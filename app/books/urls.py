from django.urls import path
from . import views


urlpatterns = [
	path('',               views.BookListView.as_view(), name='book_list'),
	path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
	path('books/add/',     views.BookCreateView.as_view(), name='book_add'),
	path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),

	path('authors/',         views.AuthorListView.as_view(), name='author_list'),
	path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
	path('authors/add/',     views.AuthorCreateView.as_view(), name='author_add'),
	path('authors/update/<int:pk>/', views.AuthorUpdateView.as_view(), name='author_update'),

	path('genres/', views.GenreListView.as_view(), name='genre_list'),
	path('genres/add/', views.GenreCreateView.as_view(), name='genre_add'),
	path('genres/update/<int:pk>/', views.GenreUpdateView.as_view(), name='genre_update')
]