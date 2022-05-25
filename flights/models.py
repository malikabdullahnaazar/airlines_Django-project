from distutils.archive_util import make_zipfile
from pickle import TRUE
from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=4)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}({self.code})"


class flight (models.Model):
    orign = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.orign}to {self.destination}"


class passanger (models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight = models.ManyToManyField(
        flight, blank=TRUE, related_name="passangers")

    def __str__(self):
        return f"{self.first} {self.last} "
