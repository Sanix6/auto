from rest_framework import serializers

from .models import Car
from ..accounts.serializers import UserSerializer


class CarSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
