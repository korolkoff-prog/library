from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['fio']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(Book)
class Book(admin.ModelAdmin):
	list_display = ['title', 'author']
