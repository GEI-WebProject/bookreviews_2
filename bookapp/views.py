from django.views.generic import ListView, DetailView
from .models import Publishing, Book

class HomeView(ListView):
    model  = Publishing
    template_name = 'home.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'