from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password])
    password_repeat = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_repeat']

    # def validate_password_repeat(self, value):
    #     if value != self.initial_data["password"]:
    #         raise ValidationError("You entered two different passwords. Please try again.")
    #     return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_repeat = attrs.pop('password_repeat')

        if password != password_repeat:
            raise ValidationError("Password aren't the same")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)