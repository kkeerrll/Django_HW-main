from django.contrib import admin
from .models import Category, Product, ModeratorGroup
from django.contrib.auth.models import Permission
from .models import ModeratorGroup

# Разрешения для модераторов
can_cancel_product = Permission.objects.get(codename='can_cancel_product')
can_change_product_description = Permission.objects.get(codename='can_change_product_description')
can_change_product_category = Permission.objects.get(codename='can_change_product_category')

# Установка разрешений для модераторской группы
moderator_group, _ = ModeratorGroup.objects.get_or_create(name='Модераторы')

moderator_group.permissions.add(can_cancel_product)
moderator_group.permissions.add(can_change_product_description)
moderator_group.permissions.add(can_change_product_category)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_published')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_editable = ('is_published',)
    actions = ['publish_products']

    def publish_products(self, request, queryset):
        queryset.update(is_published=True)
    publish_products.short_description = "Опубликовать выбранные продукты"

admin.site.register(Product, ProductAdmin)

class ModeratorGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)

admin.site.register(ModeratorGroup, ModeratorGroupAdmin)

