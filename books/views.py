from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Book
from .forms import BookForm


class HomePageView(View):
    def get(self, request):
        return render(request, "Homepage.html")

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()[:10]
        return render(request, 'booklist.html', {'books':books})

class BookCreateView(View):
    def get(self, request):
        form = BookForm
        return render(request, 'bookcreate.html', {'form':form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
        return render(request, 'bookcreate.html', {'form':form})

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        return render(request, 'details.html', {'book':book})


class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        form = BookForm(instance=book)
        return render(request, 'bookupdate.html', {'book':book, 'form':form})

    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=book.id)
        return render(request, 'bookupdate.html', {'book':book, 'form':form})


class DeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        return render(request, 'delete.html', {'book':book})

    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return redirect('books')



