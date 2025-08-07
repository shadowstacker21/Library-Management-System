from django.urls import path,include
from books.views import BookViewSet
from borrow.views import BorrowViewSet
from authors.views  import AuthorViewSet
from members.views import MemberViewSet
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('books',BookViewSet,basename='books')
router.register('authors',AuthorViewSet,basename='authors')
router.register('members',MemberViewSet,basename='members')




book_router = routers.NestedDefaultRouter(router,'books',lookup='book')
book_router.register('borrow-records',BorrowViewSet,basename='book-borrow-records')


urlpatterns = [
    path('', include(router.urls)),
    path('',include(book_router.urls)),
    

]
