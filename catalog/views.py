from django.shortcuts import render


def home_controller(request):
    return render(request, 'catalog/index.html')


def contactcontroller(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        print(f'{firstName} {lastName} {email}')
    return render(request, 'catalog/index1.html')
