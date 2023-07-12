from django.urls import path

from catalog import views

urlpatterns = [

    path('', views.home_controller),
    path('contacts/', views.contact_controller),
]
