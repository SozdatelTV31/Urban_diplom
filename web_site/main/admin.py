from django.contrib import admin
from .models import ImageFeed, DetectedObject

admin.site.register(ImageFeed)
admin.site.register(DetectedObject)