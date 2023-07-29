from django import forms
from django.utils.text import slugify

from .models import Product, BlogPost


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


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'preview', 'is_published', 'views')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(self.cleaned_data['title'])
        if commit:
            instance.save()
        return instance
