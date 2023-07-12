from django.urls import path

from catalog.views import home_controller, contactcontroller

urlpatterns = [

    path('', home_controller),
    path('contact', contactcontroller),

]
