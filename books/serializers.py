from rest_framework import serializers
from books.models import Book,BookImage

class BookImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField()
    class Meta:
        model = BookImage
        fields = ['id','image']


class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True,read_only=True)
    author_name = serializers.CharField(source='author.name',read_only=True)
    class Meta:
        model = Book
        fields = ['id','title','isbn','category','availabilty','created_at','author','author_name','images']