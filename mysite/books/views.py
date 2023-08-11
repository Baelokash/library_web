from django.shortcuts import render
from .models import Books ,Readers
#from .forms import BooksForm

def index(reguest):
    books = Books.objects.order_by('title')
    return render(reguest, "style/booksPage.html" , {'books': books})

def index2(reguest):
    person = Readers.objects.order_by('surname')
    return render(reguest, "style/readersPage.html" , {'person': person})


"""
def in_table(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
    if form.is_valid():
        selected_dish = form.cleaned_data['meat_dishes']
    else:
        form = BooksForm()

    return render(request, 'in_table.html', {'form': form})
    
"""

