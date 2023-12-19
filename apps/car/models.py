from django.db import models

from apps.accounts.models import User
from apps.category.models import Brand, Country, Category

BODY_CHOICES = (
    ('Sedan', 'Седан'),
    ('Hatchback 5dor.', 'Хэтчбек 5дв.'),
    ('SUV 5dor.', 'Внедорожник 5дв.'),
    ('Universal', 'Универсал'),
    ('Coupe', 'Купе'),
    ('Minivan', 'Минивэн'),
    ('Cabriolet', 'Кабриолет'),
)

COLOR_CHOICES = (
    ('White', 'Белый'),
    ('Black', 'Черный'),
    ('Red', 'Красный'),
    ('Yellow', 'Желтый'),
    ('Orange', 'Оранжевый'),
    ('Green', 'Зеленый'),
    ('Blue', 'Синий'),
    ('Purple', 'Фиолетовый'),
    ('Pink', 'Розовый'),
    ('Brown', 'Коричневый'),
    ('Grey', 'Серый'),
)

ENGINE_CHOICES = (
    ('Benzine', 'Бензин'),
    ('Diesel', 'Дизель'),
    ('Hybrid', 'Гибрид'),
    ('Electro', 'Электро'),
    ('Turbocharged', 'Турбированный'),
    ('Atmospheric', 'Атмосферный'),
)

TRANSMISSION_CHOICES = (
    ('Automatic', 'Автоматическая'),
    ('Mechanical', 'Механика'),
    ('Variator', 'Вариатор'),
    ('Robot', 'Робот'),
)

DRIVE_UNIT_CHOICES = (
    ('FWD', 'Передний'),
    ('RWD', 'Задний'),
    ('AWD', 'Полный'),
)

RUDDER_CHOICES = (
    ('Right', 'Правый'),
    ('Left', 'Левый'),
)

CUSTOMS_CHOICES = (
    ('Customs_cleared', 'Растоможен'),
    ('Not_Cleared_by_Customs', 'Не Растоможен'),
)


class Car(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(verbose_name='Стоимость')
    description = models.TextField(max_length=2000, verbose_name='Описание', blank=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, related_name='Марка',)
    image = models.ImageField(upload_to='car_image/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='Категория')
    year_of_issue = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег')
    body = models.CharField(max_length=50, choices=BODY_CHOICES, verbose_name='Кузов')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, verbose_name='Цвет')
    engine = models.CharField(max_length=50, choices=ENGINE_CHOICES, verbose_name='Двигатель')
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES, verbose_name='Коробка передач')
    drive_unit = models.CharField(max_length=50, choices=DRIVE_UNIT_CHOICES, verbose_name='Привод')
    rudder = models.CharField(max_length=50, choices=RUDDER_CHOICES, verbose_name='Руль')
    car_condition = models.CharField(max_length=100, verbose_name='Состояние', blank=True)
    customs = models.CharField(max_length=50, choices=CUSTOMS_CHOICES, verbose_name='Таможня')
    region = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name='Город_продажи',)
    registration = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name='Учет',)
    other = models.CharField(max_length=400, verbose_name='Прочее', blank=True)
    author = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
