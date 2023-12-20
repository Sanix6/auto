from django.views.generic import *
from .models import Car


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['title', 'price', 'description', 'brand', 'image', 'category', 'year_of_issue', 'mileage',
              'body', 'color', 'engine', 'transmission', 'drive_unit', 'rudder', 'car_condition', 'customs',
              'region', 'registration', 'other', 'author']
    success_url = '/car/create/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'detail'


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'list'



