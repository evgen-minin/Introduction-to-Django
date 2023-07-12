from django.shortcuts import render


def home_controller(request):
    return render(request, 'catalog/index.html')


def contact_controller(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        print(f"{firstname} {lastname} {email}")
    return render(request, 'catalog/contacts.html')


