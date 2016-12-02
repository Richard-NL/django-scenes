from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50, default='')
    source_location = models.ForeignKey(
        Location,
        related_name="source_location",
        on_delete=models.CASCADE
    )

    destination_location = models.ForeignKey(
        Location,
        related_name="destination_location",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s: From %s to %s'%(self.name, self.source_location, self.destination_location)
