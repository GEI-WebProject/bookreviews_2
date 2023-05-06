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
    
    
class BooksView(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'
    paginate_by = 3
    
    def get_queryset(self):
        return Book.objects.order_by('title')
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class AuthorsView(ListView):
    model  = Author
    template_name = 'authors/authors.html'
    context_object_name = 'authors'
    paginate_by = 3
    
    def get_queryset(self):
        return Author.objects.order_by('name')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'