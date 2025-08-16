from django.db import models
from authors.models import Author
from cloudinary.models import CloudinaryField
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
    
class BookImage(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='images')
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to='books/images')