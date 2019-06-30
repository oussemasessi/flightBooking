from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from flight_booking.models import Airplane, Flight, SeatConf, Passenger
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = "__all__" 

def Flight_list(request, template = 'flight_booking/Flight_list.html'):
    if request.user.is_superuser:
        Flight = Flight.objects.all()
    else:
        Flight = Flight.objects.filter(user=request.user)
    data = {}
    data['object_list'] = Flight
    return render(request, template_name, data)





