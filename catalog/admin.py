from django.contrib import admin
from .models import Author, Book, User

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author__first_name', 'author__last_name', 'borrower__name')
    list_display = ('title', 'author', 'borrowed', 'due_back', 'borrower')
    list_filter = ('borrowed', 'due_back')
