from django.urls import path,include
from members import views
from members.views import MemberViewSet
urlpatterns = [
    path('',views.MemberViewSet.as_view(),name='member-list')
]
