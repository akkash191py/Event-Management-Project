from django.db import models
from django.contrib.auth.models import User
from Events.utils import COUNTRIES


# Create your models here.
class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,  blank=False, null=False)
    contact_email = models.EmailField()
    contact_number = models.CharField(
        'Contact number', max_length=30, blank=False, null=False, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    address = models.CharField(
        "Address", max_length=255, blank=True, null=True)
    street = models.CharField("Street/Landmark", max_length=55, blank=True, null=True)
    city = models.CharField("City", max_length=255, blank=True, null=True)
    state = models.CharField("State", max_length=255, blank=True, null=True)
    postcode = models.CharField(
        "Post/Zip-code", max_length=64, blank=True, null=True)
    country = models.CharField(
        max_length=3, choices=COUNTRIES, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(("Address: {}, Street/Landmark: {}, City: {}, State: {}, Post Code: {}").format(
            self.address, self.street, self.city, self.state, self.postcode))

    class Meta:
        verbose_name_plural = 'Venue'


class Event(models.Model):
    name = models.CharField(max_length=255,  blank=False, null=False)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.ForeignKey(Organizer, related_name='Organizer', on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, related_name='Venue', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Event'


class Participant(models.Model):
    first_name = models.CharField(max_length=100,  blank=False, null=False)
    last_name = models.CharField(max_length=100,  blank=False, null=False)
    email = models.EmailField(unique=True)
    event = models.ForeignKey(Event, related_name="participants", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    class Meta:
        verbose_name_plural = 'Participant'