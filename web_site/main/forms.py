from django import forms
from .models import ImageFeed


class ImageFeedForm(forms.ModelForm):
    class Meta:
        model = ImageFeed
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-label mt-4',
                'placeholder': 'Загрузите картинку'})},
        help_texts = {
            'image': 'Добавить картинку',
        }
