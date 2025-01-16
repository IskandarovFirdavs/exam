from django.urls import path

from car.views import pricing_view

app_name = 'car'

urlpatterns = [
    path('', pricing_view, name='home'),
    ]
