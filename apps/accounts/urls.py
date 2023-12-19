from apps.accounts.views import LogoutView, LoginView, UserListView, UserDetailView, UserRegisterView
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
