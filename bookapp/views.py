from django.views.generic import ListView, DetailView
from .models import Book, Author
from django.core.cache import cache
from django.utils import timezone
from random import sample

class HomeView(ListView):
    model  = Book
    template_name = 'home.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        today = timezone.now().date()
        daily_books = cache.get(today)
        if not daily_books:
            # If the cached random books for today don't exist, generate them and cache them for the day
            all_books = list(Book.objects.all())
            daily_books = sample(all_books, 5)
            cache.set(today, daily_books, 60 * 60 * 24)  # Cache for 24 hours
        return daily_books
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'