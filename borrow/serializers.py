from rest_framework import serializers
from borrow.models import Borrow,Return



class BorrowSerializer(serializers.ModelSerializer):
    book_name=serializers.SerializerMethodField(method_name='get_book_name')
    member_name = serializers.SerializerMethodField(method_name='get_member_name')
    class Meta:
        model = Borrow
        fields = ['id','book','book_name','member','member_name','borrow_date']
        read_only_fields= ['member','borrow_date']

    def get_book_name(self,obj):
        return obj.book.title 
    def get_member_name(self,obj):
        return obj.member.get_full_name()

class ReturnSerializer(serializers.ModelSerializer):
    book_name=serializers.SerializerMethodField(method_name='get_book_name')
    member_name = serializers.SerializerMethodField(method_name='get_member_name')
    class Meta:
        model = Return
        fields = ['id','book','book_name','member','member_name','return_date']
        read_only_fields = ['member','return_date']

    def get_book_name(self,obj):
        return obj.book.title 
    
    def get_member_name(self,obj):
        return obj.member.get_full_name()

