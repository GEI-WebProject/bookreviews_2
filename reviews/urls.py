from django.urls import path
from .views import *

urlpatterns = [
    path('', ReviewListView.as_view(), name="reviews"),
    path('<int:pk>', ReviewDetailView.as_view(), name="review_detail"),
]