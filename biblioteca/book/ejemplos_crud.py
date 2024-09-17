from django.shortcuts import render

# Create your views here.
from book.models import Book

Book(
  author = "J.K. Rowling",
  title = "Harry Potter and the Philosopher's Stone",
  year = 1997,
).save()

book_data = {
    "author": "J.K. Rowling",
    "title": "Harry Potter and the Philosopher's Stone",
    "year": "1997"
}

Book(**book_data).save()  # This will also save the book to the database

books = Book.objects.all() #Select * From Books
book = Book.objects.get(pk=1) #Select * From Books where id=1
book = Book.objects.get(title = "Dracula")

books = Book.objects.filter(author="J.K. Rowling") #Select * From Books where author="J.K. Rowling"
books = Book.objects.filter(author="Bram Stoker", year = 1897) #Select * From Books where author="Bram Stoker" and year=1897

book = Book.objects.get(pk=2) #Select * From Books where id=2
book.title = "El huespued de Dracula" #Update title
book.save() 

Book.objects.all().update(title="TBA", author="Unknown")

book = Book.objects.get(pk=1)
book.delete() #Delete book with id=1

book.objects.filter(author="J.K. Rowling").delete()

book.object.all().delete() #Delete all books