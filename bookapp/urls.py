from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
]