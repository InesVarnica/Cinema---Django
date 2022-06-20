from ast import mod
from django.db import models
from django.contrib.auth.models import User
from django.views.generic import DetailView

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=30)
    display_time=models.CharField(max_length=30)
    number_of_seats=models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.movie_name, self.display_time, self.number_of_seats)

    

class Ticket(models.Model):
    seat_number=models.IntegerField()
    movie_t = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, related_name = 'ticket')
    user_t = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name = 'ticket')

    def __str__(self):
        return '%s' % (self.seat_number)







    