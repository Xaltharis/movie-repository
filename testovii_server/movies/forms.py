from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rating')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Напишите свой отзыв'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }