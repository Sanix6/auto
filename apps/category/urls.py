from django.urls import path
from .views import (CategoryCreateView, CategoryDetailView, CategoryListView,
                    BrandListView, BrandCreateView, BrandDetailView,
                    CountryDetailView, CountryListView, CountryCreateView)


urlpatterns = [
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    path('brand_create/', BrandCreateView.as_view(), name='brand_create'),
    path('brand_list/', BrandListView.as_view(), name='brand_list'),
    path('brand_detail/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),

    path('country_create/', CountryCreateView.as_view(), name='country_create'),
    path('country_list/', CountryListView.as_view(), name='country_list'),
    path('country_detail/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
]
