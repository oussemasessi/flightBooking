from django.db import models
import random
import string

# Create your models here.

class SeatConf(models.Model):
    seat_conf_id = models.AutoField(primary_key=True)
    First_Class = 'FC'
    Business_Class = 'BC'
    Economic_Class = 'EC'
    Category_Choices = [
        (First_Class, 'FC'),
        (Business_Class, 'BC'),
        (Economic_Class, 'EC'),
    ]
    category = models.CharField(
        max_length=2,
        choices=Category_Choices,
        default=Economic_Class,
    )

    def is_upperclass(self):
        return self.category in (self.First_Class, self.Business_Class, self.Economic_Class)

    rows = models.IntegerField()
    start_row = models.IntegerField()
    seats_row = models.IntegerField()
    EC_base_price = models.IntegerField()
    BC_base_price = models.IntegerField()
    FC_base_price = models.IntegerField()

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

class Seat(models.Model):
    Flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    PNR = models.IntegerField(primary_key=True)
    First_Class = 'FC'
    Business_Class = 'BC'
    Economic_Class = 'EC'
    Category_Choices = [
        (First_Class, 'FC'),
        (Business_Class, 'BC'),
        (Economic_Class, 'EC'),
    ]
    category = models.CharField(
        max_length=2,
        choices=Category_Choices,
        default=Economic_Class,
    )
    def is_upperclass(self):
        return self.category in (self.First_Class, self.Business_Class, self.Economic_Class)
    def __init__(self, category):
        self.category=category
        if category == Business_Class:
            self.PNR = '01'.join(random.choices(string.digits, k=6))
        elif category == First_Class:
            self.PNR = '02'.join(random.choices(string.digits, k=6))
        elif category == Economic_Class:
            self.PNR = '03'.join(random.choices(string.digits, k=6))

class Passenger(models.Model): 
    seat_PNR = models.ForeignKey(Seat, on_delete=models.CASCADE)      
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name, ',', self.last_name





