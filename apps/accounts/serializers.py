from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', "first_name", 'number', 'email', 'password', 'password2']

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name', ''),
            number=validated_data.get('number', ''),
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", 'number', "email", ]
