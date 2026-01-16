from django.contrib import admin
from .models import Participant, Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ("participant", "event", "confirmed", "booking_date")
    list_filter = ['confirmed',]

admin.site.register(Participant)

admin.site.register(Booking, BookingAdmin)
