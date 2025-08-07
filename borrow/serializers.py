from rest_framework import serializers
from borrow.models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['id','book','member','borrow_date','return_date']
        read_only_fields = ['borrow_date', 'return_date']