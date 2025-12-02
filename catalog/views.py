from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_products_from_cache, get_products_by_category, get_categories_with_products


class ContactsView(TemplateView):
    template_name = "contacts.html"


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "catalog/templates/contacts.html")


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"

    def get_queryset(self):
        return get_products_from_cache()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_edit.html"
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:login")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_edit.html"
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    login_url = reverse_lazy("users:login")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:login")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductsByCategoryView(ListView):
    template_name = 'products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        name = self.kwargs.get('name')
        return get_products_by_category(name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.kwargs.get('name')
        context['category'] = get_object_or_404(Category, name=name)
        context['categories'] = get_categories_with_products()
        return context


class CategoryListView(ListView):
    """Представление для отображения всех категорий"""
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return get_categories_with_products()
