from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter
from .views import PokerHandViewSet, RegisterView, UserProfileView

from .views import login_view, register_view, main_view, logout_view, post_hand_view, delete_hand_view

router = DefaultRouter()
router.register(r'pokerhands', PokerHandViewSet)

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include(router.urls)),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', main_view, name='home'),  # This will be your main page after login
    # Add other URL patterns for search, post hand history, etc.

    # path('search/', search_view, name='search'),
    path('post-hand/', post_hand_view, name='post_hand'),
    path('delete-hand/<int:hand_id>/', delete_hand_view, name='delete_hand'),
    # path('profile/', profile_view, name='profile'),
]
