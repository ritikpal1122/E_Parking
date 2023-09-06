from django.contrib import admin

from parking.models import ParkingInfo,ParkingSpace,ParkingLocation

admin.site.register(ParkingLocation)
admin.site.register(ParkingInfo)
admin.site.register(ParkingSpace)
