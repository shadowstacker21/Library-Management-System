from django.shortcuts import render
from authors.serializers import AuthorSerializer
from rest_framework.viewsets import ModelViewSet
from authors.models import Author
# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
