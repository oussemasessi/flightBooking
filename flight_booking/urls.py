from django.urls import path

from . import views

app_name = 'flight_booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('Airplane_list/<int:pk>', views.Airplane_list, name = 'Airplane_list'),
    path('Airplane_create/<int:pk>', views.Airplane_create, name = 'Airplane_create'),
    path('Flight_list/<int:pk>', views.Flight_list, name = 'Flight_list'),
    path('Flight_Create/<int:pk>', views.Flight_Create, name = 'Flight_create'),
    path('Passenger_list/<int:pk>', views.Passenger_list, name = 'Passenger_list'),
    path('Passenger_Create/<int:pk>', views.Passenger_Create, name = 'Passenger_create'),
]