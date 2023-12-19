from rest_framework import serializers

from apps.category.models import Category, Brand, Country


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["title", ]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["title", ]
