from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import (
    BlogsCreateView,
    BlogsUpdateView,
    BlogsListView,
    BlogsDetailView,
    BlogsDeleteView,
)

app_name = BlogsConfig.name


urlpatterns = [
    path("", BlogsListView.as_view(), name="blogs_list"),
    path("<int:pk>/", BlogsDetailView.as_view(), name="blogs_detail"),
    path("create/", BlogsCreateView.as_view(), name="blogs_create"),
    path("<int:pk>/update", BlogsUpdateView.as_view(), name="blogs_update"),
    path("<int:pk>/delete/", BlogsDeleteView.as_view(), name="blogs_delete"),
]
