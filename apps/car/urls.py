from django.urls import path
from .views import CarListView, CarDetailView, CarCreateView


urlpatterns = [
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('list/', CarListView.as_view(), name='car_list'),
    path('detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
