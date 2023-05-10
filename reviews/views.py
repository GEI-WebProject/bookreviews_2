from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review

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

    # TODO: Add get_queryset() method to filter reviews by book
    def get_queryset(self):
        return Review.objects.filter(book=self.kwargs['book_id'])
