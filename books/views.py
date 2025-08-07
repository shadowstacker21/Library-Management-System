from django.shortcuts import render
from books.serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from books.models import Book
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer