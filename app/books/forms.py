from django import forms
from .models import Author, Genre, Book


class BookForm(forms.Form):
	title = forms.CharField(
		min_length=3,
		max_length=255, 
		required=True, 
		label='Название книги',
		widget=forms.TextInput(
			attrs={
				'class': 'form-control', 
				'placeholder': 'Введите название книги'
			}
		) 
	)

	discription = forms.CharField(
		max_length=1000, 
		label='Описание книги', 
		widget=forms.Textarea(
			attrs = {
				'class': 'form-control', 
				'placeholder': 'Введите описание книги'
			}
		))

	author = forms.ModelChoiceField(
			queryset=Author.objects.all(),
			# to_field_name='author',
			label='Автор книги',
			widget=forms.Select(attrs={
					'class': 'form-control'
				})
		)

	genre = forms.ModelChoiceField(
			queryset=Genre.objects.all(),
			# to_field_name='genre',
			label='Жанр книги',
			widget=forms.Select(attrs={
					'class': 'form-control'
				})
		)


class BookUpdateForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'discription', 'author', 'genre']


	title = forms.CharField(
		min_length = 3,
		max_length = 255,
		required = True,
		label = 'Название книги',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Введите название книги'
				
			}
		)
	)

	discription = forms.CharField(
		max_length = 1000,
		label = 'Описание книги',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Введите описание книги'
			}
		)
	)

	author = forms.ModelChoiceField(
		queryset = Author.objects.all(),
		label = 'Автор книги',
		widget = forms.Select(
			attrs = {
				'class': 'form-control'
			}
		)
	)

	genre = forms.ModelChoiceField(
		queryset = Genre.objects.all(),
		label = 'Жанр книги',
		widget = forms.Select(
			attrs = {
				'class': 'form-control'
			}
		)
	)


class AuthorForm(forms.Form):
	fio = forms.CharField(
		min_length = 5,
		max_length = 255,
		required = True,
		label = 'ФИО автора',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Введите ФИО писателя'
			}
		)
	)

	bio = forms.CharField(
		max_length = 1000,
		label = 'Краткая биография',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Введите краткую биографию писателя'
			}
		)
	)

	birth_date = forms.DateField(
		label = 'Дата рождения писателя',
		widget = forms.SelectDateWidget(
			attrs = {
				'class': 'form-control'
			}
		)
	)

	death_date = forms.DateField(
		label = 'Дата смерти писателя',
		widget = forms.SelectDateWidget(
			attrs = {
				'class': 'form-control'
			}
		)
	)


class AuthorUpdateForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ['fio', 'bio', 'birth_date', 'death_date']

	fio = forms.CharField(
		min_length = 5,
		max_length = 255,
		required = True,
		label = 'ФИО автора',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control'
			}
		)
	)

	bio = forms.CharField(
		max_length = 1000,
		label = 'Краткая биография',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control'
			}
		)
	)

	birth_date = forms.DateField(
		label = 'Дата рождения писателя',
		widget = forms.SelectDateWidget(
			attrs = {
				'class': 'form-control'
			}
		)
	)

	death_date = forms.DateField(
		label = 'Дата смерти писателя',
		widget = forms.SelectDateWidget(
			attrs = {
				'class': 'form-control'
			}
		)
	)


class GenreForm(forms.Form):
	name = forms.CharField(
		min_length = 3,
		max_length = 50,
		required = True,
		label = 'Название жанра',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Введите название жанра'
			}
		)
	)


class GenreUpdateForm(forms.ModelForm):
	class Meta:
		model = Genre
		fields = ['name']

	name = forms.CharField(
		min_length = 3,
		max_length = 50,
		required = True,
		label = 'Название жанра',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Введите название жанра'
			}
		)
	)