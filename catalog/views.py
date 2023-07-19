from django.shortcuts import render

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


def card_product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/card_product.html', context)
