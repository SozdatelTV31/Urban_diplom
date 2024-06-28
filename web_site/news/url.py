from django.urls import path
from .import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ViewingPost.as_view(), name='news-post'),
    path('<int:pk>/update', views.UpdatePost.as_view(), name='news-update'),
    path('<int:pk>/delete', views.DeletePost.as_view(), name='news-delete')
]