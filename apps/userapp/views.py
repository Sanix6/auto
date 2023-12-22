from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.userapp.models import *
from django.contrib import messages
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import *


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if User.objects.filter(email=request.data["email"]).exists():
            return Response(
                {
                    "response": False,
                    "message": "Пользователь с таким электронным адресом уже существует.",
                }
            )

        if serializer.is_valid():
            email = serializer.data["email"]
            first_name = serializer.data["first_name"]
            last_name = serializer.data["last_name"]
            password = serializer.data["password"]
            phone = serializer.data["phone"]

            user = User(
                email=email, first_name=first_name, last_name=last_name, phone=phone
            )
            user.set_password(password)
            user.save()


            return Response({"response": True, "message": "Код подверждения отправлено на вашу почту!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)