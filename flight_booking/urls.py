from django.urls import path

from . import views

app_name = 'flight_booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('Airplane_list/<int:pk>', views.Airplane_list, name = 'Airplane_list'),
    path('Airplane_create/<int:pk>', views.Airplane_create, name = 'Airplane_create'),
    path('SeatConf_create/<int:pk>', views.SeatConf_Create, name = 'SeatConf_create'),
    path('Flight_list/<int:pk>', views.Flight_list, name = 'Flight_list'),
    path('Flight_create/<int:pk>', views.Flight_create, name = 'Flight_create'),
    #path('Passenger_list/<int:pk>', views.Passenger_list, name = 'Passenger_list'),
    #path('Passenger_create/<int:pk>', views.Passenger_create, name = 'Passenger_create'),
    path('reserve_seat/<int:pk>', views.reserve_seat, name = 'reserve_seat'),
    
]