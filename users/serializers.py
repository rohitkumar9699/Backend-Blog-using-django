from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
import re


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        error_messages={'required': 'Username is required.'}
    )
    email = serializers.EmailField(
        required=True,
        error_messages={'required': 'Email is required.'}
    )
    phone = serializers.CharField(
        required=True,
        error_messages={'required': 'Phone number is required.'}
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'},
        error_messages={'required': 'Password is required.'}
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password')

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        # Simple regex check to ensure '@' is present
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Invalid email format.")
        return value

    def validate_phone(self, value):
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number is already in use.")
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

    def create(self, validated_data):
        try:
            user = CustomUser.objects.create_user(**validated_data)
        except DjangoValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone')
