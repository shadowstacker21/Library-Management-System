from django.urls import path,include
from authors import views
from authors.views import AuthorViewSet
urlpatterns = [
    path('',views.AuthorViewSet.as_view(),name='author-list')
]
