from django.core.cache import cache

from .models import Product, Category

from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    """
    Получаем данные по продуктам из кэша либо формируем кэш и тянем данные из БД
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(name=None):
    """
    функция для получения продуктов по категории
    """
    try:
        if name:
            category = Category.objects.get(name=name)
        else:
            return Product.objects.none()

        return Product.objects.filter(
            category=category,
            is_published=True
        ).select_related('category', 'owner')

    except Category.DoesNotExist:
        return Product.objects.none()


def get_categories_with_products():
    """Получение всех категорий"""
    return Category.objects.filter(products__is_published=True).distinct()