from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'price': 'Цена',
            'image': 'Изображение',
            'category': 'Категория',
        }
