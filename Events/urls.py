from django.urls import path, include
from Events.views import (
                        OrganizerListCreateAPIView, 
                        EventListCreateAPIView, 
                        EventDetailAPIView, 
                        VenueListCreateAPIView, 
                        VenueDetailAPIView, 
                        ParticipantListCreateAPIView, 
                        ParticipantDetailAPIView
                    )



urlpatterns = [

    # Events App Urls
    
    path('organizer_details/', OrganizerListCreateAPIView.as_view(), name='organizer-list'),
    path('venues/', VenueListCreateAPIView.as_view(), name='venue-list'),
    path('venues/<int:pk>/', VenueDetailAPIView.as_view(), name='venue-detail'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('participants/', ParticipantListCreateAPIView.as_view(), name='participant-list'),
    path('participant/<int:pk>/', ParticipantDetailAPIView.as_view(), name='participant-detail'),
    
]