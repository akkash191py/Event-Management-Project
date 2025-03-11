from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from UserAccount.models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from django.utils.encoding import smart_str, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
import logging
from phonenumber_field.modelfields import PhoneNumberField


#Write your Own serializer
class UserRegSerializer(serializers.Serializer):
    first_name= serializers.CharField(required=True,min_length=3)
    last_name= serializers.CharField(required=True,min_length=3)
    email = serializers.EmailField(required=True)
    mobile = PhoneNumberField(blank=False, null=False, unique=True)
    gender = serializers.CharField(required=True,min_length=3)
    role = serializers.CharField(required=True,min_length=3)
    

    def validate_email(self, email):
        check_email = User.objects.filter(email=email).first()
        if check_email:
            raise serializers.ValidationError("Email already exists!")
        return email
    
    def validate_mobile(self, mobile):
        check_mobile = User.objects.filter(mobile=mobile).first()
        if check_mobile:
            raise serializers.ValidationError("Mobile No already exists!")
        return mobile



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,min_length=6)


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True,min_length=6)
    new_password = serializers.CharField(required=True,min_length=6)
