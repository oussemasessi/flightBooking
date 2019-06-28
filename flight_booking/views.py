from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from flight_booking.models import Airplane

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AirplaneForm(ModelForm):
    class Meta:
        model = Airplane
        fields = "__all__" 


def Airplane_list(request):
    Airplanes = Airplane.objects.all()
    return render(request, 'Airplane_list.html', {'Airplanes': Airplanes})

def Airplane_create(request):
    if request.POST:
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_booking.views.Airplane_list')
    else:
        form = AirplaneForm()
    return render(request, 'Airplane_create.html', {'form': form})


def Airplane_update(request, id_user):
    Airplane = get_object_or_404(Airplane, id=id_Airplane)
    form = AirplaneForm(request.POST or None, instance=Airplane)
    if form.is_valid():
        form.save()
        return redirect('flight_booking.views.Airplane_list')
    return render(request, "Airplane_create.html", {'form': form})


def Airplane_delete(request, id_user):
    Airplane = Airplane.objects.get(id=id_Airplane)
    Airplane.delete()
    return redirect('flight_booking.views.Airplane_list')

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = "__all__" 

