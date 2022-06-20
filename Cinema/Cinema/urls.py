"""Cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', views.get_movies,name='movies'),
    path('ticket/', views.get_tickets),
    path('create/', views.create_data),
    path('buy_tickets/', views.buy_tickets),
    path('buy_ticket/<int:movie_id>', views.buy_ticket, name='buy_ticket'),
    path('ticket_per_user/<int:user_id>', views.get_ticket_by_id,name='mytickets'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>', views.delete_movie, name='delete_movie'),
    path('edit_movie/<int:movie_id>', views.edit_movie, name='edit_movie'),
    path('ticket_per_projection/<int:movie_id>', views.get_ticket_by_movie_id, name='ticket_per_projection'),
    path('ticket_per_projection_user/<int:movie_id>', views.get_ticket_by_movie_id_user, name='ticket_per_projection_user'),
    path('data/', views.get_data, name='data')
    
    
    
]
