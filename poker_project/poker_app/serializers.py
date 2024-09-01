from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PokerHand

class PokerHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokerHand
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
""" 
    User details: 
    username: Hillman
    password: Yy8529637

    token:
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTIyNjU4NSwiaWF0IjoxNzI1MTQwMTg1LCJqdGkiOiJiNDhmZDlhYWM0ZWE0ZWQ2OWMxZjFiNjE4YzZlOTNhNiIsInVzZXJfaWQiOjJ9.Szqd5W7KexHxqLzCdJ5F6VeAyO5lQA21XPXtgTp10fQ",
    (the access token is the authorization token you need)
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MTQwNDg1LCJpYXQiOjE3MjUxNDAxODUsImp0aSI6IjlhNjI0NDI2ZjllMjQ4MTZiZWVlZGNjYTJmZjc4Yjk5IiwidXNlcl9pZCI6Mn0.tSh4rDZkDGL9OONQ-DKARIxFE9s-joeZQQfbiXtYmDc"
"""

# run in terminal using this 
# curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MTQwNDg1LCJpYXQiOjE3MjUxNDAxODUsImp0aSI6IjlhNjI0NDI2ZjllMjQ4MTZiZWVlZGNjYTJmZjc4Yjk5IiwidXNlcl9pZCI6Mn0.tSh4rDZkDGL9OONQ-DKARIxFE9s-joeZQQfbiXtYmDc" http://localhost:8000/api/profile/

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']