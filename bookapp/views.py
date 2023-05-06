from django.views.generic import ListView, DetailView
from .models import Book, Author

class HomeView(ListView):
    model  = Book
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 3
    
    def get_queryset(self):
        return Book.objects.order_by('?')
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'