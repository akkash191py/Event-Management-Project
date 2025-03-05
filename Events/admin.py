from django.contrib import admin
from .models import Organizer, Venue, Event, Participant

# Register your models here.
class OrganizerAdmin(admin.ModelAdmin):
    list_display=["name","contact_email","contact_number"]
    search_fields = ["name", "contact_email", "contact_number"]
admin.site.register(Organizer, OrganizerAdmin)


class VenueAdmin(admin.ModelAdmin):
    list_display=["address","street","city", "state", "postcode", "country"]
    
admin.site.register(Venue, VenueAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display=["name","description","start_time", "end_time", "organizer"]
    
admin.site.register(Event, EventAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","email", "event"]
    
admin.site.register(Participant, ParticipantAdmin)

