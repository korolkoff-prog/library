from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
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


def book_add(request):
	form = BookForm()

	if request.method == "POST":
		book = Book()
		form = BookForm(request.POST)
		
		if form.is_valid():
			book.title = form.cleaned_data['title']
			book.discription = form.cleaned_data['discription']
			book.author = form.cleaned_data['author']
			book.genre  = form.cleaned_data['genre']
			book.save()
			return redirect('book_list')
	
	return render(request, 'books/add_book.html', {'form': BookForm()})


def book_update(request, pk):
	book = get_object_or_404(Book, pk=pk)

	if request.method == "POST":
		form = BookUpdateForm(request.POST)
		if form.is_valid():
			book.title = form.cleaned_data['title']
			book.discription = form.cleaned_data['discription']
			book.author = form.cleaned_data['author']
			book.genre = form.cleaned_data['genre']
			book.save()
			return redirect('book_list')

	return render(request, 'books/update_book.html', {'form': BookUpdateForm(instance=book)})



class AuthorListView(ListView):
	model = Author
	template_name = 'books/author_list.html'
	context_object_name = 'authors'
	paginate_by = 10


class AuthorDetailView(DetailView):
	model = Author
	template_name = 'books/author_detail.html'
	context_object_name = 'author'


def author_add(request):
	form = AuthorForm()

	if request.method == "POST":
		author = Author()
		form = AuthorForm()

		if form.is_valid():
			author.fio = form.cleaned_data['fio']
			author.bio = form.cleaned_data['bio']
			author.birth_date = form.cleaned_data['birth_date']
			author.death_date = form.cleaned_data['death_date']
			author.save()
			return redirect('author_list')

	return render(request, 'books/add_author.html', {'form': AuthorForm()})


def author_update(request, pk):
	author = get_object_or_404(Author, pk=pk)

	if request.method == "POST":
		form = AuthorUpdateForm(request.POST)
		if form.is_valid():
			author.fio = form.cleaned_data['fio']
			author.bio = form.cleaned_data['bio']
			author.birth_date = form.cleaned_data['birth_date']
			author.death_date = form.cleaned_data['death_date']
			author.save()
			return redirect('author_list')

	return render(request, 'books/update_author.html', {'form': AuthorUpdateForm(instance=author)})



class GenreListView(ListView):
	model = Genre
	template_name = 'books/genre_list.html'
	context_object_name = 'genres'


def genre_add(request):
	form = GenreForm()

	if request.method == "POST":
		genre = Genre()
		form = GenreForm()

		if form.is_valid():
			genre.name = form.cleaned_data['name']
			genre.save()
			return redirect('genre_list')

	return render(request, 'books/add_genre.html', {'form': form})


def genre_update(request, pk):
	genre = get_object_or_404(Genre, pk=pk)

	if request.method == "POST":
		form = GenreUpdateForm(request.POST)
		if form.is_valid():
			genre.name = form.cleaned_data['name']
			genre.save()
			return redirect('genre_list')

	return render(request, 'books/update_genre.html', {'form': GenreUpdateForm(instance=genre)})



