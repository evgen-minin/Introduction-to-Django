from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Продукты'


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
