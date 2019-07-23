from django.contrib import admin
from flight_booking.models import *

# Register your models here.
admin.site.register(Airplane)
admin.site.register(Flight)
admin.site.register(SeatConf)
admin.site.register(BookedSeat)
admin.site.register(Seat)