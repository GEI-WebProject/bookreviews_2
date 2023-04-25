from django.views.generic import ListView, DetailView
from .models import Publishing
from random import random

class HomeView(ListView):
    model  = Publishing
    template_name = 'home.html'
    context_object_name = 'publishings'
    paginate_by = 3
    
    def get_queryset(self):
        return Publishing.objects.order_by('?')
        


class BookDetailView(DetailView):
    model = Publishing
    template_name = 'book_detail.html'
    context_object_name = 'publishing'