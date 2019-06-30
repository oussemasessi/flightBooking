from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from flight_booking.models import Airplane, Flight, SeatConf, Passenger, Seat
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AirplaneForm(ModelForm):
    class Meta:
        model = Airplane
        fields = "__all__" 


def Airplane_list(request, template = 'flight_booking/Airplane_list.html'):
    Airplanes = Airplane.objects.all()
    data = {}
    data['object_list'] = Airplanes
    return render(request, 'Airplane_list.html', data)

def Airplane_create(request):
    if request.POST:
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_booking.views.Airplane_list')
    else:
        form = AirplaneForm()
    return render(request, 'Airplane_create.html', {'form': form})

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = "__all__" 

def Flight_list(request, template = 'flight_booking/Flight_list.html'):
    Flights = Flight.objects.all()
    data = {}
    data['object_list'] = Airplanes
    return render(request, 'Airplane_list.html', data)

def Flight_Create(request):
    if request.POST:
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_booking.views.Flight_list')
    else:
        form = FlightForm()
    return render(request, 'Flight_create.html', {'form': form})

class SeatConfForm(ModelForm):
    class Meta:
        model = SeatConf
        fields = "__all__" 

def SeatConf_list(request, template = 'flight_booking/SeatConf_list.html'):
    SeatConfs = SeatConf.objects.all()
    data = {}
    data['object_list'] = SeatConfs
    return render(request, 'SeatConf_list.html', data)

def SeatConf_Create(request):
    if request.POST:
        form = SeatConfForm(request.POST)
        if form.is_valid():
            form.save()
            if (category == 'EC'):
                self.EC_base_price = int(input())
            elif (category == 'BC'):
                self.BC_base_price = int(input())
            elif (category == 'FC'):
                self.FC_base_price = int(input()) 
            return redirect('flight_booking.views.SeatConf_list')
    else:
        form = SeatConfForm()
    return render(request, 'SeatConf_create.html', {'form': form})

class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = "__all__" 

def Passenger_list(request, template = 'flight_booking/Passenger_list.html'):
    Passengers = Passenger.objects.all()
    data = {}
    data['object_list'] = Passengers
    return render(request, 'Passenger_list.html', data)

def Passenger_Create(request):
    if request.POST:
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_booking.views.Passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'Passenger_create.html', {'form': form})

'''class Seat(ModelForm)

def Choose_Seat(request):
    if request.POST:

'''


