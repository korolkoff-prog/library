from django.urls import path
from . import views


urlpatterns = [
	path('',               views.BookListView.as_view(), name='book_list'),
	path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
	path('books/add/',     views.book_add, name='book_add'),
	path('books/update/<int:pk>/', views.book_update, name='book_update'),

	path('authors/',         views.AuthorListView.as_view(), name='author_list'),
	path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
	path('authors/add/',     views.author_add, name='author_add'),
	path('authors/update/<int:pk>/', views.author_update, name='author_update'),

	path('genres/', views.GenreListView.as_view(), name='genre_list'),
	path('genres/add/', views.genre_add, name='genre_add'),
	path('genres/update/<int:pk>/', views.genre_update, name='genre_update')
]