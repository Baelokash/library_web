"""
from django import forms
from .models import Books

class BooksForm(forms.Form):
    meat_dishes = forms.ModelChoiceField(
    queryset=Books.objects.filter(Books__title='Название', Books__author='Автор').distinct(),
    label='Книги'
)
"""