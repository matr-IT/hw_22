
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, contact_form

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
