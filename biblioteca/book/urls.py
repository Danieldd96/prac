from django.urls import path
from .views import CreateBookView,ListBookView

urlpatterns = [
    path("create_book/", CreateBookView.as_view(), name="create_book"),
    path('all/',ListBookView.as_view(), name="books_list")
]
