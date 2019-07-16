from django.db import models

# Create your models here.

class Passenger(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat_PNR = models.ForeignKey(Seat, on_delete=models.CASCADE)      
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name, ',', self.last_name





