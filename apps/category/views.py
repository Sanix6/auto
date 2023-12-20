from rest_framework import generics
from .models import Category, Brand, Country
from .serializers import CategorySerializer, BrandSerializer, CountrySerializer
from django.views.generic import CreateView, DetailView, ListView


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_create.html'
    fields = ['title']
    success_url = '/category/category_create/'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    field = ['title']
    success_url = '/category/category_detail'


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    field = ['title']
    success_url = '/category/category_list'


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brand_create.html'
    fields = ['title']
    success_url = '/category/brand_create/'


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    field = ['title']
    success_url = '/brand/brand_detail'


class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    fields = ['title']
    success_url = '/brand/brand_list'


class CountryCreateView(CreateView):
    model = Country
    template_name = 'country_create.html'
    fields = ['title']
    success_url = '/category/country_create/'


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class CountryListView(ListView):
    model = Country
    template_name = 'country_list.html'
    fields = ['title']
    success_url = '/country/country_list'
