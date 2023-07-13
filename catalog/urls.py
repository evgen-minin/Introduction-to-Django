from django.urls import path

from catalog.views import home_controller, contact_controller

urlpatterns = [

    path('', home_controller),
    path('contacts/', contact_controller, name='contacts'),
]
