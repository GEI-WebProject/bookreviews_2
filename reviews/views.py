from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review

class ReviewListView(ListView):
    model = Review
    template_name = "reviews/reviews.html"
    context_object_name = "reviews"

class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/review_detail.html"
    context_object_name = "review"    