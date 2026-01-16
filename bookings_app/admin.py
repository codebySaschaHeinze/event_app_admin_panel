from django.contrib import admin
from .models import Participant, Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ("participant", "event", "confirmed", "booking_date")
    list_filter = ['confirmed',]
    readonly_fields = ('booking_date',)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("full_name", "first_name", "last_name", "email")
    readonly_fields = ("full_name",)

    def save_model(self, request, obj, form, change):
        obj.full_name = f"{obj.first_name} {obj.last_name}".strip()
        super().save_model(request, obj, form, change)

admin.site.register(Participant, ParticipantAdmin)

admin.site.register(Booking, BookingAdmin)
