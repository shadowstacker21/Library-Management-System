from authors.models import Author
from rest_framework import serializers
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','biography']
        read_only_fields = ['name','biography']

class AddAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'        

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['biography']