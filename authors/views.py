from django.shortcuts import render
from authors.serializers import AuthorSerializer,UpdateSerializer,AddAuthorSerializer
from rest_framework.viewsets import ModelViewSet
from authors.models import Author
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Create your views here.

class AuthorViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = Author.objects.all()
    def get_permissions(self):
        if self.request.method == 'GET':
           return [IsAuthenticated()]
        else:
            return [IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddAuthorSerializer
        if self.request.method == 'PATCH':
            return UpdateSerializer
        return AuthorSerializer
        
