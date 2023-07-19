from django.urls import path

from catalog.views import card_product, home_controller, contact_controller


urlpatterns = [
    path('', home_controller, name='home'),
    path('contacts/', contact_controller, name='contacts'),
    path('catalog/', card_product, name='catalog'),
]
