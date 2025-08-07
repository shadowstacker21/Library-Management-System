from django.shortcuts import render
from borrow.serializers import BorrowSerializer
from borrow.models import Borrow
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from members.models import Member
from django.utils import timezone
from django.shortcuts import get_object_or_404

class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
   

    @action(detail=False, methods=['post'], url_path='borrow')
    def borrow_book(self, request, book_pk=None):
        member_id = request.data.get('member_id')
        try:
            book = Book.objects.get(id=book_pk)
            if not book.availabilty:
                return Response({'error': 'Book not available'}, status=status.HTTP_400_BAD_REQUEST)
            member = Member.objects.get(id=member_id)

            borrow = Borrow.objects.create(book=book, member=member)
            book.availabilty = False
            book.save()

            return Response(self.get_serializer(borrow).data, status=status.HTTP_201_CREATED)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except Member.DoesNotExist:
            return Response({'error': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='return')
    def return_book(self, request, pk=None):
        borrow = get_object_or_404(Borrow, pk=pk)
        if borrow.return_date:
            return Response({'error': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)

        borrow.return_date = timezone.now()
        borrow.save()

        borrow.book.availabilty = True
        borrow.book.save()

        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)