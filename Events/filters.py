import django_filters
from Events.models import Event, Organizer, Participant

class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    organizer__name = django_filters.CharFilter(lookup_expr='icontains')
    
    

    class Meta:
        model = Event
        fields = ['name', 'organizer__name']


class ParticipantFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    event = django_filters.CharFilter(lookup_expr='icontains')
    
    

    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'email', 'event']
         