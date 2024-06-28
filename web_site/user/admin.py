from django.contrib import admin
from .models import User
from django.apps import AppConfig

admin.site.register(User)


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
