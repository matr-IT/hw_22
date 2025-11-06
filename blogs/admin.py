from django.contrib import admin
from .models import Blogs

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'created_at', 'views_count']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'body']
    readonly_fields = ['created_at', 'views_count']