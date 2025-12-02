from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    ProductsListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, ProductsByCategoryView, CategoryListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:name>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]
