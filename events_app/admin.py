from django.contrib import admin
from .models import EventCategory, Location, Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'date')
    search_fields = ('title', 'date')
    list_filter = ['category']
    date_hierarchy = 'date'

    fieldsets = (
        ('Allgemein',{
            'fields': ('title', 'category', 'date'),
        }),

        ('Organisation', {
            'fields': ('location', 'capacity'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(EventCategory)

admin.site.register(Location)

admin.site.register(Event, EventAdmin)
