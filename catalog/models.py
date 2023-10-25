# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.core.cache import cache
from django.db import models


class MyModel(models.Model):
    # поля модели

    def get_cached_data(self):
        # Пробуем получить данные из кеша
        data = cache.get(f'my_key_{self.id}')

        # Если данные найдены в кеше, возвращаем их
        if data:
            return data

        # Если данных нет в кеше, выполняем логику обработки и сохраняем результат в кеш
        data = expensive_operation()
        cache.set(f'my_key_{self.id}', data, timeout=3600)  # Сохраняем данные в кеш на 1 час

        return data


class ModeratorGroup(Group):
    pass

class Meta:
    proxy = True
    verbose_name = 'Группа модераторов'
    verbose_name_plural = 'Группы модераторов'



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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

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

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.PositiveIntegerField()
    version_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
