from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ReviewForm

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
    
class BookReviewsCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book_id = self.kwargs['book_id']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('book_reviews', kwargs={'book_id': self.kwargs['book_id']})

    