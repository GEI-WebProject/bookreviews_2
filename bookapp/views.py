from django.views.generic import ListView
from .models import Book

class HomeView(ListView):
    model  = Book
    template_name = 'home.html'

