from django.core.validators import MinLengthValidator
from rest_framework import serializers

from .validators import number_validator, letter_validator, special_char_validator
from ..base.serializers import BaseModelSerializer
from .models import User, Profile


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'is_active', 'is_admin', 'created_at', 'updated_at', 'password', 'confirm_password'
        )

    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        validators=[
            number_validator,
            letter_validator,
            special_char_validator,
            MinLengthValidator(limit_value=8)
        ], write_only=True
    )
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('username already taken')
        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already taken')
        return email

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError('Please fill password and confirm password')

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError('confirm password is not equal to password')

        data.pop('confirm_password', None)
        return data
