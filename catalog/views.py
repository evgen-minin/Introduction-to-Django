from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from catalog.forms import ProductForm
from catalog.models import Product


def home_controller(request):
    return render(request, 'catalog/home.html')


def contact_controller(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        print(f"{firstname} {lastname} {email}")

        return render(request, 'catalog/success.html')

    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/card_product.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:card_product')
