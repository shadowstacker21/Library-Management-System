from django.db import models
from books.models import Book
from users.models import User
# Create your models here.
class Borrow(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowed_books')
    member = models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrowed_members')
    borrow_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name} borrowed {self.book.title}"
    
class Return(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='returned_books')
    member = models.ForeignKey(User,on_delete=models.CASCADE,related_name='returned_members')
    return_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name} return by {self.book.title}"
    

