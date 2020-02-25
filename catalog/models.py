from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    borrowed = models.BooleanField(default=False)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name