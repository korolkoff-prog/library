from django.db import models


class Author(models.Model):
	fio = models.CharField('ФИО автора', max_length=255, db_index=True)
	bio = models.TextField('Биография автора', max_length=1000)
	birth_date = models.DateField('Дата рождения', blank=True)
	death_date = models.DateField('Дата смерти', blank=True)

	def __str__(self):
		return self.fio

	class Meta:
		ordering = ['fio']
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'


class Genre(models.Model):
	name = models.CharField('Название жанра', max_length=50, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'


class Book(models.Model):
	title = models.CharField('Название книги', max_length=255, db_index=True)
	discription = models.TextField('Описание книги', max_length=1000, blank=True)
	author = models.ForeignKey(Author, verbose_name='Автор книги', on_delete=models.SET_NULL, null=True)
	genre  = models.ForeignKey(Genre, verbose_name='Жанр книги', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'