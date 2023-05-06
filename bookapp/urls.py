from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books', BooksView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('authors', AuthorsView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
]