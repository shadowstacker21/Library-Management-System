from django.urls import path,include
from borrow import views
urlpatterns = [
    path('',views.BorrowReturnDetailsView.as_view(),name='book-list'),
     
]
