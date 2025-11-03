from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Содержание")
    image = models.ImageField(
        upload_to="blogs/photo", blank=True, verbose_name="Превью", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        choices=[("draft", "Черновик"), ("published", "Опубликовано")],
    )
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = [
            "name",
        ]
