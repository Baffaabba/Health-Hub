from django.shortcuts import render, redirect, reverse

#imports
from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from authentication.models import UserDetails

from authentication.serializers import (
    AuthTokenSerializer,
    UserProfileSerializer, 
    UserRegSerializer
    )

class UserRegistration(CreateAPIView):
    """Create new user view"""
    serializer_class = UserRegSerializer
    
    
class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileView(generics.RetrieveUpdateAPIView):
    """Retrive and Update authenticated user profile"""
    serializer_class = UserProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrive and return authenticated user"""

        return UserDetails.objects.get(user=self.request.user) 
    
class GenerateOtpView(GenericAPIView):
    # serializer_class = 
    pass