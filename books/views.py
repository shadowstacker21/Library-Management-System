from django.shortcuts import render
from books.serializers import BookSerializer,BookImageSerializer
from rest_framework.viewsets import ModelViewSet
from books.models import Book,BookImage
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .paginations import DefaultPagination
# Create your views here.

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    pagination_class = DefaultPagination
    search_filter = ['name','authors__name']
    ordering_filter = ['id']
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def get_queryset(self):
        return Book.objects.select_related('author').prefetch_related('images').all()


class BookImageViewSet(ModelViewSet):
    serializer_class = BookImageSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]
    def get_queryset(self):
        return BookImage.objects.filter(book_id=self.kwargs.get('book_pk'))
    
    def perform_create(self, serializer):
         serializer.save(book_id=self.kwargs.get('book_pk'))