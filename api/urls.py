from django.urls import path,include
from books.views import BookViewSet,BookImageViewSet
from borrow.views import BorrowView,ReturnView
from authors.views  import AuthorViewSet

from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('books',BookViewSet,basename='books')
router.register('authors',AuthorViewSet,basename='authors')


book_router = routers.NestedDefaultRouter(router,'books',lookup='book')
book_router.register('images',BookImageViewSet,basename='book-images')
book_router.register('borrow-book',BorrowView,basename='borrow-book')
book_router.register('return-book',ReturnView,basename='return-bbok')

urlpatterns = [
    path('', include(router.urls)),
    path('',include(book_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    

]
