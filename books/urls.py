from django.urls import path
from .views import HomePageView, BookListView, BookCreateView, \
    BookDetailView, BookUpdateView, DeleteView, BookSearchView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='books'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('search/', BookSearchView.as_view(), name='search'),
]