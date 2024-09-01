from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from rest_framework import viewsets, generics
from .models import PokerHand
from .serializers import PokerHandSerializer, UserSerializer, UserProfileSerializer
from .froms import PokerHandForm
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    Everyone else can only view the object.
    """

    def has_permission(self, request, view):
        # Allow anyone to view the list of objects or retrieve a single object
        if view.action in ['list', 'retrieve']:
            return True
        # Only allow authenticated users to perform other actions
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow anyone to view the object
        if view.action in ['retrieve']:
            return True
        # Only allow the owner to edit or delete the object
        return obj.user == request.user
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register


    
class PokerHandViewSet(viewsets.ModelViewSet):

    """ This setup ensures that:

    Only the owner of a poker hand can view, edit, or delete it.
    When a new hand is created, it is automatically associated with the currently authenticated user.
    
    """
        
    queryset = PokerHand.objects.all()
    serializer_class = PokerHandSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Save the user who created the hand as the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Everyone can view all hands, but the owner can filter to only their hands if needed
        return PokerHand.objects.all()
    

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the main page after successful login
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
            return render(request, 'poker_app/login.html')
    else:
        return render(request, 'poker_app/login.html')
    
def logout_view(request):
    logout(request)  # This function logs out the user
    return redirect('login')

def register_view(request):
    return render(request, 'poker_app/register.html')

@login_required
def main_view(request):
    poker_hands = PokerHand.objects.all().order_by('-created_at')  # Retrieve all poker hands, ordered by creation date
    return render(request, 'poker_app/main.html', {'poker_hands': poker_hands})


@login_required
def post_hand_view(request):
    if request.method == 'POST':
        form = PokerHandForm(request.POST)
        if form.is_valid():
            poker_hand = form.save(commit=False)
            poker_hand.user = request.user
            poker_hand.save()
            return redirect('home')  # Redirect to the main page after posting
    else:
        form = PokerHandForm()
    
    return render(request, 'poker_app/post_hand.html', {'form': form})

@login_required
def delete_hand_view(request, hand_id):
    poker_hand = get_object_or_404(PokerHand, id=hand_id)

    if request.user == poker_hand.user:
        poker_hand.delete()
        return redirect('home')
    else:
        # Optionally, handle unauthorized deletion attempts
        return redirect('home')