from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductsListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products_list/", ProductsListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
