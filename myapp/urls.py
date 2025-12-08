from django.urls import path
from .views import books,book

urlpatterns = [
    path('books/',books),
    path('book/<id>',book)
]
