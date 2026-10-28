from django.contrib import admin
from .models import Room, Guest, Service, Booking


admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Service)
admin.site.register(Booking)

# Register your models here.
