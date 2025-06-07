from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm, BookUpdateForm, AuthorUpdateForm, GenreUpdateForm


class BookListView(ListView):
	model = Book
	template_name = 'books/book_list.html'
	context_object_name = 'books'
	paginate_by = 10


class BookDetailView(DetailView):
	model = Book
	template_name = 'books/book_detail.html'
	context_object_name = 'book'


class BookCreateView(CreateView):
	model = Book
	form_class = BookForm
	template_name = 'books/add_book.html'
	success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
	model = Book
	form_class = BookUpdateForm
	template_name = 'books/update_book.html'
	success_url = reverse_lazy('book_list')



class AuthorListView(ListView):
	model = Author
	template_name = 'books/author_list.html'
	context_object_name = 'authors'
	paginate_by = 10


class AuthorDetailView(DetailView):
	model = Author
	template_name = 'books/author_detail.html'
	context_object_name = 'author'


class AuthorCreateView(CreateView):
	model = Author
	form_class = AuthorForm
	template_name = 'books/add_author.html'
	success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
	model = Author
	form_class = AuthorUpdateForm
	template_name = 'books/update_author.html'
	success_url = reverse_lazy('author_list')



class GenreListView(ListView):
	model = Genre
	template_name = 'books/genre_list.html'
	context_object_name = 'genres'


class GenreCreateView(CreateView):
	model = Genre
	form_class = GenreForm
	template_name = 'books/add_genre.html'
	success_url = reverse_lazy('genre_list')


class GenreUpdateView(UpdateView):
	model = Genre
	form_class = GenreUpdateForm
	template_name = 'books/update_genre.html'
	success_url = reverse_lazy('genre_list')
