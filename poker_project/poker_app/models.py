from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class PokerHand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    stack_size = models.DecimalField(max_digits=10, decimal_places=2)
    hand_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
