from django.contrib.auth import (
    get_user_model,
    )
from rest_framework import serializers
from django.utils.translation import gettext as _
from authentication.models import UserDetails

class UserRegSerializer(serializers.ModelSerializer):
    """serializer for user model"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'passwords': {'write_only': True, 'min_length':5}}

    def create(self, validated_data):
        """create and return user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
    

    
class AuthTokenSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=True,
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        try:
            user_obj = get_user_model().objects.get(email=email)
            if user_obj.check_password(password):
                user = user_obj
            else:
                user = None
        except get_user_model().DoesNotExist:
            user = None

        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

class UserDatailsLink(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'is_staff', 'is_driver']
        depth = 1
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserDatailsLink(read_only=True)
    class Meta:
        model = UserDetails
        fields = ['age', 'phone', 'user']