from django.contrib import admin
from borrow.models import Borrow,Return
# Register your models here.

admin.site.register(Borrow)
admin.site.register(Return)