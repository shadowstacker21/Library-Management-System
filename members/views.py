from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from members.models import Member
from members.serializers import MemberSerializer
# Create your views here.
class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer