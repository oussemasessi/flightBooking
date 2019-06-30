from django.db import models
import random
import string

# Create your models here.

class SeatConf(models.Model):
    seat_conf_id = models.IntegerField(primary_key=True)
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

    def __init__(self, category, rows, seats_row, start_row):
        self.category = category
        self.rows = rows
        self.seats_row = seats_row
        self.start_row = start_row
        if (category == 'EC'):
            self.EC_base_price = int(input())
        elif (category == 'BC'):
            self.BC_base_price = int(input())
        elif (category == 'FC'):
            self.FC_base_price = int(input()) 



class Airplane(models.Model):
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
    
    P_Capacity = models.PositiveIntegerField()
    seat_conf_id = models.ForeignKey(SeatConf, on_delete=models.CASCADE)
    seats_remaining = [P_Capacity]
    
'''    def __init__(self, Ptype, SeatConf):
        if (P_type in type_Choices):
            self.P_type = Ptype
        self.P_Capacity = SeatConf.seats_row * SeatConf.rows
        self.seats_remaining = []
        for row_number in range(SeatConf.start_row, Airplane.P_Capacity + SeatConf.start_row):
            for seat_number in range(SeatConf.seats_row):
                self.seats_remaining.append(Seat(row_number, seat_number))
'''

class Passenger(models.Model): 
    PNR = ''.join(random.choices(string.digits, k=8))      
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name, ',', self.last_name


class Seat(models.Model):
    plane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    seat_PNR = models.ForeignKey(Passenger, on_delete=models.CASCADE)
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
    def __init__(self, category=None):
        self.category=category


class Flight(models.Model):
    airplane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    origin = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)



