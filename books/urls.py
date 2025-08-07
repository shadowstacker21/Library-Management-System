from django.urls import path,include
from books import views
urlpatterns = [
    path('',views.BookViewSet.as_view(),name='book-list')
]
