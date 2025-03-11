from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from Events.models import Organizer, Venue, Event, Participant
from Events.serializers import OrganizerSerializer, VenueSerializer, EventSerializer, ParticipantSerializer
from Events.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from Events.filters import EventFilter, ParticipantFilter





# Organizer List API
class OrganizerListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

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

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(events, request)
        venueserializerData = VenueSerializer(venue, many=True)
        return Response(venueserializerData.data)

    def put(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        venueserializerData = VenueSerializer(venue, data=request.data)
        if venueserializerData.is_valid():
            venueserializerData.save()
            return Response(venueserializerData.data)
        return Response(venueserializerData.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Event List API
class EventListCreateAPIView(APIView):

    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(events, request)
        filterset = EventFilter(request.GET, queryset=events)      # Apply Filter

        if filterset.is_valid():
            events = filterset.qs  # Get filtered queryset

        
        EventserializerData = EventSerializer(events, many=True)
        return paginator.get_paginated_response(EventserializerData.data)

    def post(self, request):
        request.data['created_by'] = request.user.id
        EventserializerData = EventSerializer(data=request.data)

        if request.user.role == "Admin":

            if EventserializerData.is_valid():
                EventserializerData.save()
                return Response({"status": "success", "message":"Participant data Created successfully", "data":  EventserializerData.data}, status=status.HTTP_201_CREATED)

            return Response(EventserializerData.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"status": "warning", "message":"You don't have permission to Create Events",}, status=status.status.HTTP_403_FORBIDDEN)

# Event Detail API
class EventDetailAPIView(APIView):

    
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = get_object_or_404(Event, pk=pk)

        if event.created_by != request.user:
            return Response({"error": "You do not have permission to edit this event."}, status=status.HTTP_403_FORBIDDEN)

        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","message":"Event data Updated successfully","data": serializer.data}, status=200) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if event.created_by != request.user:
            return Response({"error": "You do not have permission to delete this event."}, status=status.HTTP_403_FORBIDDEN)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Participant List API
class ParticipantListCreateAPIView(APIView):

    
    permission_classes = [IsAuthenticated]

    def get(self, request):

        participantObj = Participant.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(participantObj, request)

        filterset = ParticipantFilter(request.GET, queryset=participantObj)      # Apply Filter

        if filterset.is_valid():
            participantObj = filterset.qs  # Get filtered queryset

        participantserializer = ParticipantSerializer(participantObj, many=True)
        return paginator.get_paginated_response(participantserializer.data)

    # def post(self, request):
    #     participantserializer = ParticipantSerializer(data=request.data)
    #     if participantserializer.is_valid():
    #         participantserializer.save()
    #         return Response({"status": "success", "message":"Participant data Created successfully", "data":  participantserializer.data}, status=status.HTTP_201_CREATED)
    #     return Response(participantserializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Participant Detail API
class ParticipantDetailAPIView(APIView):

    
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        participantObj = get_object_or_404(Participant, pk=pk)
        serializer = ParticipantSerializer(participantObj)
        return Response(serializer.data)

    def put(self, request, pk):
        participantObj = get_object_or_404(Participant, pk=pk)
        participantserializer = ParticipantSerializer(participantObj, data=request.data, partial=True)

        if participantObj.user != request.user.id:
            return Response({"error": "You do not have permission to edit this event."}, status=status.HTTP_403_FORBIDDEN)

        if participantserializer.is_valid():
            participantserializer.save()
            return Response({"status": "success","message":"Participant data Updated successfully","data":  participantserializer.data}, status=200)
        return Response(participantserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        participantObj = get_object_or_404(Participant, pk=pk)

        if participantObj.user != request.user.id:
            return Response({"error": "You do not have permission to delete this event."}, status=status.HTTP_403_FORBIDDEN)

        participantObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    