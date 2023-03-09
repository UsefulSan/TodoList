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

    def validate_password_repeat(self, value):
        if value != self.initial_data["password"]:
            raise ValidationError("You entered two different passwords. Please try again.")
        return value

    def create(self, validated_data):
        validated_data.pop('password_repeat')
        return User.objects.create_user(**validated_data)


class UserProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)


class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=False, max_length=30)
    new_password = serializers.CharField(required=False, max_length=30, validators=[validate_password])

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate(self, data):
        if not self.context['request'].user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Wrong password'})
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save(update_fields=['password'])
        return instance


