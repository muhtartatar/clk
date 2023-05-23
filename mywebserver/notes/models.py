from django.db import models

class WeekNote(models.Model):
    day_of_week = models.CharField(max_length=10)
    note_title = models.CharField(max_length=100)
    note_description = models.TextField()
