#the login_required decorator
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from flight_booking.models import *
from django.http import HttpResponse
from django import forms


def index(request):
    return HttpResponse("Hello, world. You're at the flight booking index.")

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
            if (Economic_Class):
                self.EC_rows = int(input())
                self.EC_start_row = int(input())
                self.EC_seats_row = int(input())
                self.EC_base_price = int(input())
            elif (First_Class):
                self.FC_rows = int(input())
                self.FC_start_row = int(input())
                self.FC_seats_row = int(input())
                self.FC_base_price = int(input())
            elif (Business_Class):
                self.BC_rows = int(input())
                self.BC_start_row = int(input())
                self.BC_seats_row = int(input())
                self.BC_base_price = int(input()) 
            form.save()
            return redirect('flight_booking.views.SeatConf_list')
    else:
        form = SeatConfForm()
    return render(request, 'SeatConf_create.html', {'form': form})

class AirplaneForm(ModelForm):
    class Meta:
        model = Airplane
        fields = "__all__" 

def Airplane_list(request, template = 'flight_booking/Airplane_list.html'):
    Airplanes = Airplane.objects.all()
    data = {}
    data['object_list'] = Airplanes
    return render(request, 'Airplane_list.html', data)

def Airplane_create(request, seat_conf_id):
    try:
        seat_conf_info = SeatConf.objects.get(pk=seat_conf_id)
    except Show.DoesNotExist:
        raise Http404("Page Does Not Exist.")
    if request.POST:
        form = AirplaneForm(request.POST)
        if form.is_valid():
            print("hello")
            for category in seat_conf_info.categories:
                if (category == 'Economic Class'):
                    for row in seat_conf_info.EC_rows:
                        for seat in seat_conf_info.EC_seats_row:
                            PNR = '01'.join(random.choices(string.digits, k=6))
                            start_row = seat_conf_info.EC_start_row
                            new_seat = Seat.objects.create_seat(category, PNR, seat_row + start_row, seat)
                            print(new_seat)
                            new_seat.save()
                elif (category == 'First Class'):
                    for row in seat_conf_info.FC_rows:
                        for seat in seat_conf_info.FC_seats_row:
                            PNR = '02'.join(random.choices(string.digits, k=6))
                            start_row = seat_conf_info.FC_start_row
                            new_seat = Seat.objects.create_seat(category, PNR, row + start_row, seat)
                            new_seat.save()
                elif (category == 'Business Class'):
                    for row in seat_conf_info.BC_rows:
                        for seat in seat_conf_info.BC_seats_row:
                            PNR = '03'.join(random.choices(string.digits, k=6))
                            start_row = seat_conf_info.BC_start_row
                            new_seat = Seat.objects.create_seat(category, PNR, row + start_row, seat)  
                            new_seat.save()
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
    data['object_list'] = Flights
    return render(request, 'Flight_list.html', data)

def Flight_create(request):
    if request.POST:
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('flight_booking.views.Flight_list')
    else:
        form = FlightForm()
    return render(request, 'Flight_create.html', {'form': form})

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ('category',)

class SelectedSeatForm(forms.Form):
    selected_seat = forms.CharField(required=True,max_length=10,help_text='Seat No seperated by ,')

@login_required
def reserve_seat(request, flight_id):
    try:
        flight_info = Flight.objects.get(pk=flight_id)
    except Show.DoesNotExist:
        raise Http404("Page Does Not Exist.")
    form  = SeatForm()
    form2 = SelectedSeatForm()
    context = {'flight_info':flight_info,'form':form,'form2':form2}

    return render(request,'flight_booking/reserve_seat.html',context)


@login_required
def payment_gateway(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        category = request.POST.get('category')
        flight_id = request.POST.get('flight_id')

        flight = Flight.objects.get(pk=flight_id)
        seats = seats.split(',')
        book_seat = []
        for each in seats:
            try:
                #if seat not found in DB
                s = Seat.objects.get(category=category,no=each, flight=flight)
            except:
                #redirect to seatnotfound.html
                return Http404

            if Seat.objects.filter(category=category,no=each,flight=flight):
                s = Seat(no=each,category=category,flight=flight)
                book_seat.append(s)

        form = BookingForm()

        price_rate = 1000 #Yes.
        ticket_price = price_rate * len(book_seat)

        #Creating the seat string.
        seat_str = ""
        for i in range(len(seats)):
            if i == len(seats)-1:
                seat_str += seats[i]
            else:
                seat_str += seats[i] + ','

        context = {'seats': seat_str,'seat_type':seat_type,'show':show,'form':form,'ticket_price':ticket_price}
        return render(request,'booking/payment_gateway.html',context)
    else:
        return redirect('dashboard.views.home')

'''
class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = "__all__" 

def Passenger_list(request, template = 'flight_booking/Passenger_list.html'):
    Passengers = Passenger.objects.all()
    data = {}
    data['object_list'] = Passengers
    return render(request, 'Passenger_list.html', data)

def Passenger_create(request):
    if request.POST:
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_booking.views.Passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'Passenger_create.html', {'form': form})


def Passenger_select_seat(request):
    for seat in Airplane.seats_remaining:
        if not Airplane.seats_remaining[seat]: Airplane.seats_remaining.append(Seat.__init__())
'''
