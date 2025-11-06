from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


def home(request):
    return render(request, "home.html")


class ContactsView(TemplateView):
    template_name = "contacts.html"


# def contacts(request):
#     return render(request, "contacts.html")


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "catalog/templates/contacts.html")


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
