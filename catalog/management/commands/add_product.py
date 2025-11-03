from unicodedata import category

from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="smartphones", description="smart telephones with full-touch displays"
        )
        products = [
            {
                "name": "iphone",
                "description": "A smartphone from Apple",
                "category": category,
                "price": 100000,
            },
            {
                "name": "samsung",
                "description": "A smartphone not from Apple",
                "category": category,
                "price": 80000,
            },
            {
                "name": "xiaomi",
                "description": "A smartphone also not from Apple",
                "category": category,
                "price": 60000,
            },
        ]

        for p in products:
            product, created = Product.objects.get_or_create(**p)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен продукт:{product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукт уже существует:{product.name}")
                )

