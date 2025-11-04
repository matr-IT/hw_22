from django.db import models


class Blogs(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    PUBLISH_STATUS = [
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    ]

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Содержание")
    photo = models.ImageField(
        upload_to="blogs/photo",
        blank=True,
        verbose_name="Превью",
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.CharField(
        max_length=20,
        choices=PUBLISH_STATUS,
        default=DRAFT,
        verbose_name="Статус публикации"
    )

    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ["title"]