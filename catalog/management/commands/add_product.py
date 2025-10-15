from unicodedata import category

from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='cat_1', description='123')
        products = [
            {'name': 'iphone', 'description': 123, 'category': category, 'price': 100},
            {'name': 'samsung', 'description': 321, 'category': category, 'price': 80}
        ]

        for p in products:
            product, created = Product.objects.get_or_create(**p)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Успешно добавлен продукт:{product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует:{product.name}'))
