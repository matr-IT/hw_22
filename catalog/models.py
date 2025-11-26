from django.conf import settings
from django.db import models
from django.db.models import BooleanField, CASCADE

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="владелец продукта"
    )
    is_published = BooleanField(default=False, verbose_name="Продукт опубликован?")

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
        ]
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
            ("can_delete_product", "can delete product"),
        ]
