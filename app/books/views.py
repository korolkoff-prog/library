from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm, BookUpdateForm, AuthorUpdateForm, GenreUpdateForm


def book_list(request):
	books = Book.objects.all()
	return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'books/book_detail.html', {'book': book})


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


def author_list(request):
	authors = Author.objects.all()
	return render(request, 'books/author_list.html', {'authors': authors})


def author_detail(request, pk):
	author = get_object_or_404(Author, pk=pk)
	return render(request, 'books/author_detail.html', {'author': author})


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


def genre_list(request):
	genres = Genre.objects.all()
	return render(request, 'books/genre_list.html', {'genres': genres})


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



