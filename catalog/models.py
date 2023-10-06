# Create your models here.

from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='Нет описания')


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='Нет описания')
    image = models.ImageField(upload_to='product_images/', default='default_image.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания будет автоматически заполняться при создании объекта
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения будет автоматически обновляться при сохранении объекта

    def __str__(self):
        return self.name



class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog/posts/previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
