from django import forms
from .models import PokerHand

class PokerHandForm(forms.ModelForm):
    class Meta:
        model = PokerHand
        fields = ['position', 'stack_size', 'hand_history']
