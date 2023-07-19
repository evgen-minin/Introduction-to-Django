from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import card_product, home_controller, contact_controller, create_product


urlpatterns = [
    path('', home_controller, name='home'),
    path('contacts/', contact_controller, name='contacts'),
    path('catalog/', card_product, name='catalog'),
    path('create/', create_product, name='create_product')
]
