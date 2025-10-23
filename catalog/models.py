from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(
        upload_to="catalog/photo", blank=True, verbose_name="изображение", null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.IntegerField(verbose_name="цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата последнего изменения"
    )

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
        ]
