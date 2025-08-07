from django.db import models
from books.models import Book
from members.models import Member
# Create your models here.
class Borrow(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,name='book')
    member = models.ForeignKey(Member,on_delete=models.CASCADE,name='member')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.name}"