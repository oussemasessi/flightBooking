from django.urls import path

from . import views

app_name = 'flight_booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('Flight_list/<int:pk>', views.Flight_list, name = 'Flight_list'),
    path('Flight_Create/<int:pk>', views.Flight_Create, name = 'Flight_create'),
    path('Passenger_list/<int:pk>', views.Passenger_list, name = 'Passenger_list'),
    path('Passenger_Create/<int:pk>', views.Passenger_Create, name = 'Passenger_create'),
]