from django.shortcuts import render

from catalog.models import Product


def home_controller(request):
    latest_products = Product.objects.order_by('-created_date')[:5]
    for product in latest_products:
        print(product.name)

    return render(request, 'catalog/index.html')


def contact_controller(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        print(f"{firstname} {lastname} {email}")

        return render(request, 'catalog/success.html')

    return render(request, 'catalog/contacts.html')
