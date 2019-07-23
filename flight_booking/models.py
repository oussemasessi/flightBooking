from django.db import models
import random
import string

# Create your models here.

class SeatConf(models.Model):
    seat_conf_id = models.AutoField(primary_key=True)

    Business_Class = 'Business Class'
    BC_rows = models.IntegerField()
    BC_start_row = models.IntegerField()
    BC_seats_row = models.IntegerField()
    BC_base_price = models.IntegerField()

    First_Class = 'First Class'
    FC_rows = models.IntegerField()
    FC_start_row = models.IntegerField()
    FC_seats_row = models.IntegerField()
    FC_base_price = models.IntegerField()    

    Economic_Class = 'Economic Class'
    EC_rows = models.IntegerField()
    EC_start_row = models.IntegerField()
    EC_seats_row = models.IntegerField()
    EC_base_price = models.IntegerField()

    categories = [Economic_Class, First_Class, Business_Class]
     

class Airplane(models.Model):
    P_Capacity = models.PositiveIntegerField()
    seat_conf_id = models.ForeignKey(SeatConf, on_delete=models.CASCADE)
    seats_remaining = [P_Capacity]  
    Boeing = 'boeing'
    Airbus = 'airbus'
    Jet = 'jet'
    type_Choices =[
        (Boeing, 'bg'),
        (Airbus, 'as'),
        (Jet, 'jt'),
    ]
    P_type = models.CharField(
        max_length=6, 
        choices=type_Choices,
        default=Airbus,
    )
    def is_upperclass(self):
        return self.P_type in (self.Boeing, self.Airbus, self.Jet)              

class Flight(models.Model):
    airplane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    origin = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)

class SeatManager(models.Manager):
    def create_seat(self, category, PNR, row_number, seat_number):
        seat = self.create(category=category, PNR=PNR, row_number=row_number, seat_number=seat_number)
        '''if category == Business_Class:
            seat.PNR = '01'.join(random.choices(string.digits, k=6))
        elif category == First_Class:
            seat.PNR = '02'.join(random.choices(string.digits, k=6))
        elif category == Economic_Class:
            seat.PNR = '03'.join(random.choices(string.digits, k=6))'''
        return seat

class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    PNR = models.IntegerField(primary_key=True)
    #row_number = models.IntegerField()
    #seat_number = models.IntegerField()

    First_Class = 'First_Class'
    Business_Class = 'Business_Class'
    Economic_Class = 'Economic_Class'
    Category_Choices = [
        (First_Class, 'First_Class'),
        (Business_Class, 'Business_Class'),
        (Economic_Class, 'Economic_Class'),
    ]
    category = models.CharField(
        max_length=14,
        choices=Category_Choices,
        default=Economic_Class,
    )
    def is_upperclass(self):
        return self.category in (self.First_Class, self.Business_Class, self.Economic_Class)

    def PNR_generator(category):
        if (category == 'Economic Class'):
            PNR = '01'.join(random.choices(string.digits, k=6))
        
    
    objects = SeatManager()

class BookedSeat(models.Model):
    seat_PNR = models.ForeignKey(Seat, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat_PNR', 'flight')

    def __str__(self):
        return str(self.seat_PNR) + '|' + str(self.flight)


'''
class Passenger(models.Model): 
    seat_PNR = models.ForeignKey(Seat, on_delete=models.CASCADE)      
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name, ',', self.last_name
'''





