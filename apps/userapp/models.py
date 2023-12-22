from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    is_active = models.BooleanField('Активный', default=False)
    code = models.IntegerField("Код активации", null=True, blank=True)

    email = models.EmailField('Эл-почта (логин)', unique=True)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    phone = models.CharField('Телефон номер', max_length=50)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"