from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from bookapp.models import Book

class AllReviewsListView(ListView):
    model = Review
    template_name = "reviews/reviews.html"
    context_object_name = "reviews"

class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/review_detail.html"
    context_object_name = "review"

class BookReviewsListView(ListView):
    model = Review
    template_name = "reviews/book_reviews.html"
    context_object_name = "reviews"
    paginate_by = 2

    # Add get_queryset() method to filter reviews by book
    def get_queryset(self):
        return Review.objects.filter(book=self.kwargs['book_id'])
    
    # Add get_context_data() method to add book to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context
