
from itertools import count
import numbers
from re import A, M, T
from shutil import move
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Movie,Ticket,User
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from .forms import TicketForm, MovieForm
from django.contrib.auth.decorators import login_required 
from django.db.models import Count
from django.db.models.functions import Lower
from collections import OrderedDict


# Create your views here


@login_required
def get_movies(request):
    movies=Movie.objects.all()
    return render(request, 'movies.html',{"data":movies})

def get_tickets(request):
    tickets=Ticket.objects.all()
    return render(request, 'tickets.html',{"data":tickets})

def get_ticket_by_id(request, user_id):
    ticket_by_id = Ticket.objects.filter(user_t=user_id)
    return render(request, 'ticket_per_user.html', {"data":ticket_by_id})

def get_ticket_by_movie_id(request, movie_id):
    ticket_by_id = Ticket.objects.filter(movie_t=movie_id)
    return render(request, 'tickets_per_projection.html', {"data":ticket_by_id})

def get_ticket_by_movie_id_user(request, movie_id):
    ticket_by_id = Ticket.objects.filter(movie_t=movie_id)
    return render(request, 'tickets_per_projection_and_user.html', {"data":ticket_by_id})

def create_data(request):
    m1 = Movie(movie_name="Harry Potter", display_time=19.00,number_of_seats=100)
    m2 = Movie(movie_name="Spiderman", display_time=18.00,number_of_seats=90)
    m3 = Movie(movie_name="Avatar", display_time=19.00,number_of_seats=80)
    m1.save()
    m2.save()
    m3.save()
    return HttpResponse('<h1>Done</h1>')

#Vjezba 7#
def buy_tickets(request):

    user=User.objects.get(pk=6)
    projection=Movie.objects.get(pk=14)
    print(user)
    print(projection)
    all_seats_per_projection=Ticket.objects.filter(movie_t=projection)
    br=0
    for seat_number in all_seats_per_projection:
        br=br+1

    if br<50:
        ticket=Ticket(seat_number=br+1,movie_t=projection,user_t=user)
        ticket.save()
        new_number_of_seats=(projection.number_of_seats-1)
        projection.number_of_seats=new_number_of_seats
        projection.save()
    else:
        pass
    
    ticket_by_id = Ticket.objects.filter(user_t=2)
    print(ticket_by_id)
    return HttpResponse('<h1>Done</h1>')

def register(request):
    if request.method == 'GET':
        userForm = UserCreationForm()
        return render(request, 'register.html', {'form':userForm})
    elif request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        return HttpResponseNotAllowed('Not able to save!')




#Vjezba 8#
def buy_ticket(request, movie_id):
    
    user_id = request.user.id
    user=User.objects.get(pk=user_id)
    projection=Movie.objects.get(pk=movie_id)
    all_seats_per_projection=Ticket.objects.filter(movie_t=projection)
    br=0
    entry_list = list(Ticket.objects.filter(movie_t=projection))
    counter=Ticket.objects.filter(movie_t=projection).count()
    print(counter)
    #print(len(entry_list))
    

    
    for seat_number in all_seats_per_projection:
        br=br+1

    if br<50:
        ticket=Ticket(seat_number=br+1,movie_t=projection,user_t=user)
        ticket.save()
        new_number_of_seats=(projection.number_of_seats-1)
        projection.number_of_seats=new_number_of_seats
        projection.save()
        return redirect('movies')
    else:
        return redirect('login')
        



    
    


@login_required
def add_movie(request):
    if request.method == 'GET':
        movieForm = MovieForm()
        return render(request, 'add_movie.html', {"form":movieForm})
    elif request.method == 'POST':
        movieForm = MovieForm(request.POST)
        if movieForm.is_valid():
            movieForm.save()
            cleaned_data = movieForm.cleaned_data
            #print(cleaned_data)
            return redirect('movies')
        else:
            return redirect('login')

@login_required
def edit_movie(request,movie_id):
    movie_by_id = Movie.objects.get(id=movie_id)
    if request.method == 'GET':
        data_to_update = MovieForm(instance=movie_by_id)
        return render(request, 'edit_movie.html', {"form":data_to_update})
    elif request.method == 'POST':
        data_to_update = MovieForm(request.POST, instance=movie_by_id)
        if data_to_update.is_valid():
            data_to_update.save()
            return redirect('movies')
    else:
        return HttpResponse("Something went wrong!")


def delete_movie(request, movie_id):
    movie_by_id = Movie.objects.get(id=movie_id)
    print(request.POST)
    if request.method == 'GET':
        movie_by_id.delete()
        return redirect('movies')
    


#Vjezba za obranu#
def get_data(request):
    movie=Movie.objects.annotate(Count('ticket')).filter(ticket__seat_number__gte=15)
    movie=Movie.objects.all().filter(ticket__seat_number=10)
    movie=Movie.objects.annotate(Count('ticket')).filter(ticket__user_t__gte=14)
    movie = Movie.objects.alias(tickets=Count('ticket')).filter(tickets__gt=10)
    movie=Ticket.objects.all().order_by('movie_t__movie_name')
    movie=Movie.objects.order_by(Lower('movie_name').desc())
    movie=Movie.objects.all().filter(ticket__user_t__username='ante1').distinct
    movie = Ticket.objects.all().select_related('movie_t')
    movie = Movie.objects.alias(tickets=Count('ticket')).filter(tickets__gte=14)
    movie = Ticket.objects.annotate(Count('movie_t'))
    ticket = User.objects.all()
    moviee = ticket.annotate(num_kartas=Count('ticket')).order_by('-num_kartas')[:5]
    
    user=User.objects.all()

    listaa=[]
    for x in moviee:
        for y in user:
            if str(x) == str(y.id):
                listaa.append(y)

   


        
    
    

    return render(request, 'data.html' ,{'data':moviee})