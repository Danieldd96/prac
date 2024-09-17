from django.shortcuts import render
from django.views.generic import CreateView,ListView
from book.models import Book

class CreateBookView(CreateView):
    model = Book
    fields = ["author","title","year"]
    template_name = "createBook.html"
    
class ListBookView(ListView):
    mode = Book
    queryset = Book.objects.all()
    template_name = "books.html"