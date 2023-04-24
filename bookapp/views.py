from django.views.generic import ListView
from .models import Publishing

class HomeView(ListView):
    model  = Publishing
    template_name = 'home.html'

