from django.db import models
from authors.models import Author
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=100,unique=True)
    category = models.CharField(max_length=200)
    availabilty = models.BooleanField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,name='author')

    def __str__(self):
        return self.title