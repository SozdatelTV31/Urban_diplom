from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = models.CharField('Ваш пол', max_length=50, blank=True)
    birthdate = models.CharField('Дата вашего рождения', max_length=50, blank=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)