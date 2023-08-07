
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)  # new
from django.views.generic import ListView, DetailView  # new
from django.shortcuts import render, redirect  # new
from .models import Book
from django.db.models import Q  # new
from .forms import WorkForm


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'  # new
    template_name = 'books/book_list.html'
    login_url = 'account_login'  # new


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'  # new
    permission_required = 'books.special_status'  # new


class SearchResultsListView(ListView):  # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))
        

# class CreateWork(ListView):  # работает незнаю как добавить формы
#     model = Book
#     template_name = 'books/create.html'


def post_create(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    form = WorkForm()
    context = {
        'form': form
    }
    return render(request, 'books/create.html', context)
