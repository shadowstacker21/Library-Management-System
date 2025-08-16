from django.shortcuts import render
from borrow.serializers import BorrowSerializer,ReturnSerializer
from borrow.models import Borrow,Return
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.exceptions import ValidationError

class BorrowView(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
    serializer_class = BorrowSerializer
    queryset = Borrow.objects.select_related('book').select_related('member').all()

    def get_permissions(self):
        if self.request.method.upper() in ['GET', 'POST']:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def perform_create(self, serializer):
        user = self.request.user
        book=serializer.validated_data['book']
        with transaction.atomic():
            book = Book.objects.select_for_update().get(id=book.id)
            if not book.availabilty:
                raise ValidationError("This book is currently unavailable.")
            if Borrow.objects.filter(book=book,member=user).exists():
                raise ValidationError("You have already borrowed this book.")
        
            book.availabilty = False
            book.save()
            serializer.save(member=user)

class ReturnView(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
    serializer_class = ReturnSerializer
    queryset = Return.objects.select_related('book').select_related('member').all()
    

    def get_permissions(self):
        if self.request.method.upper() in ['GET', 'POST']:
            return [IsAuthenticated()]
        return [IsAdminUser()]
    
    def perform_create(self, serializer):
        user = self.request.user
        book = serializer.validated_data['book']

        with transaction.atomic():
            borrow = Borrow.objects.filter(book=book, member=user).first()
            if not borrow:
                raise ValidationError("You did not borrow this book.")
            
            if Return.objects.filter(book=book, member=user).exists():
                raise ValidationError("You have already returned this book.")

            book.availabilty = True
            book.save()
            serializer.save(member=user)
