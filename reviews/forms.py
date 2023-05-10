from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    CHOICES = [(i, str(i)) for i in range(1, 5+1)]
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': 1,
        'cols': 2,
        }), max_length=20)
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4,
        'cols': 3,
        }))
    rating = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=CHOICES, initial=1)
    
    class Meta:
        model = Review
        fields = ['title', 'body', 'rating']
        