from django.core.cache import cache
from catalog.models import Category


def get_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('categories', list(categories))
    return categories
