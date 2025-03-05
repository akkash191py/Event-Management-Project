from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from Events.models import Organizer, Venue, Event, Participant
from Events.serializers import OrganizerSerializer, VenueSerializer, EventSerializer, ParticipantSerializer





# Organizer List API
class OrganizerListCreateAPIView(APIView):

    def get(self, request):
        organizerData = Organizer.objects.all()
        organizerserializer = OrganizerSerializer(organizerData, many=True)
        return Response(organizerserializer.data)


# Venue List API
class VenueListCreateAPIView(APIView):
    def get(self, request):
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Venue Detail API
class VenueDetailAPIView(APIView):
    def get(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        serializer = VenueSerializer(venue)
        return Response(serializer.data)

    def put(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        serializer = VenueSerializer(venue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Event List API
class EventListCreateAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Event Detail API
class EventDetailAPIView(APIView):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Participant List API
class ParticipantListCreateAPIView(APIView):
    def get(self, request):
        participantObj = Participant.objects.all()
        participantserializer = ParticipantSerializer(participantObj, many=True)
        return Response(participantserializer.data)

    def post(self, request):
        participantserializer = ParticipantSerializer(data=request.data)
        if participantserializer.is_valid():
            participantserializer.save()
            return Response(participantserializer.data, status=status.HTTP_201_CREATED)
        return Response(participantserializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Participant Detail API
class ParticipantDetailAPIView(APIView):
    def get(self, request, pk):
        participantObj = get_object_or_404(Participant, pk=pk)
        serializer = ParticipantSerializer(participantObj)
        return Response(serializer.data)

    def put(self, request, pk):
        participantObj = get_object_or_404(Participant, pk=pk)
        participantserializer = ParticipantSerializer(participantObj, data=request.data)
        if participantserializer.is_valid():
            participantserializer.save()
            return Response(participantserializer.data)
        return Response(participantserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        participantObj = get_object_or_404(Participant, pk=pk)
        participantObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    


# {
# "address" : "H.no 413, Sastur",
# "street" : "Sparsh hospital",
# "city" : "Pune",
# "state" : "MH",
# "postcode" : "413606",
# "country" : "IN"
# }