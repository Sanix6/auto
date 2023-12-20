from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from .models import User
from .permissions import IsSuperuserOrReadOnly, IsOwnerOrReadOnly
from .serializers import UserRegisterSerializer, UserSerializer
from django.contrib.auth import logout
from django.shortcuts import render


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({"detail": "Successfully logged in."})
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


class DisallowCreateIfLoggedInMixin(APIView):
    def perform_authentication(self, request):
        user = self.request.user
        if user and user.is_authenticated:
            self.permission_denied(
                request,
                message="You are already logged in. Account creation is not allowed."
            )


class UserRegisterView(DisallowCreateIfLoggedInMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        return render(request, 'myapp/user_list.html', {'object_list': users})


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()
        return Response({'message': 'User successfully updated.'})

    def perform_destroy(self, instance):
        instance.delete()
        return Response({'message': 'User successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)

