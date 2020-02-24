from django.contrib import admin

# Register your models here.
from .models import Author, User, Book, BookInstance

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(BookInstance)