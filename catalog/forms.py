from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import Product, BlogPost, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'owner']
        exclude = ('owner',)
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'price': 'Цена',
            'image': 'Изображение',
            'category': 'Категория',
        }
        
    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError('Запрещенное слово в названии продукта.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError('Запрещенное слово в описании продукта.')
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current_version']
        labels = {
            'product': 'Продукт',
            'version_number': 'Номер версии',
            'version_name': 'Название версии',
            'is_current_version': 'Текущая версия',
        }

    def clean_is_current_version(self):
        is_current_version = self.cleaned_data['is_current_version']
        product = self.cleaned_data.get('product')

        if is_current_version and product:
            active_versions = Version.objects.filter(product=product, is_current_version=True)
            if self.instance and self.instance.pk:
                active_versions = active_versions.exclude(pk=self.instance.pk)
            if active_versions.exists():
                raise forms.ValidationError('Может быть только одна активная версия продукта.')
        return is_current_version


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview', 'is_published', 'views')
        labels = {
            'title': 'Заголовок',
            'content': 'Содержимое',
            'preview': 'Изображение',
            'is_published': 'Дата создания',
            'views': 'Количество просмотров'
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(self.cleaned_data['title'])
        if commit:
            instance.save()
        return instance
