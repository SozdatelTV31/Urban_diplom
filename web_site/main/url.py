from django.urls import path
from .views import home, naro_pic, process, add, delete, gates, about
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', gates, name='gates'),
    path('home', home, name='home'),
    path('naro_pic/', naro_pic, name='naro_pic'),
    path('process/<int:feed_id>/', process, name='process_feed'),
    path('add-image-feed/', add, name='add_image_feed'),
    path('image/delete/<int:image_id>/', delete, name='delete_image'),
    path('about', about, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
