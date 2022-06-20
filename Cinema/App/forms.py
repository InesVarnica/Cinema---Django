from django.forms import ModelForm
from .models import Ticket, Movie


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['seat_number', 'movie_t','user_t']


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name', 'display_time','number_of_seats']

