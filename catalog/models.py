
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from users.models import User

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

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')
    
    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Продукты'

    @property
    def active_version(self):
        return self.versions.filter(is_current_version=True).first()


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


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    version_name = models.CharField(max_length=100)
    is_current_version = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - Version {self.version_number}"
