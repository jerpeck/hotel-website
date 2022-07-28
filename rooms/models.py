from django.db import models

# Create your models here.

class Amenity(models.Model):
    amenity_name = models.CharField(max_length=25)

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    view = models.CharField(max_length=2, choices=[('OC', 'Ocean View'), ('MT', 'Mountain View')])
    amenities = models.ManyToManyField(Amenity)
    room_image = models.ImageField()
    room_description = models.TextField()
    room_rate = models.DecimalField(decimal_places=2)