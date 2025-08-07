from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        model = Book
        fields = ['id','title','isbn','category','availabilty','created_at','author_name']