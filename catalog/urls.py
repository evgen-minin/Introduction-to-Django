from django.urls import path

from catalog.views import home_controller, contact_controller, ProductListView, ProductCreateView

urlpatterns = [
    path('', home_controller, name='home'),
    path('contacts/', contact_controller, name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('create/', ProductCreateView.as_view(), name='create_product')
]
