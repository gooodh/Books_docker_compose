
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)  # new
from django.views.generic import ListView, DetailView, CreateView  # new
from django.shortcuts import render, redirect  # new
from .models import Book
from django.db.models import Q  # new
from .forms import BookForm


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'  # new
    template_name = 'books/book_list.html'
    # login_url = 'account_login'  # new


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    # login_url = 'account_login'  # new
    # permission_required = 'books.special_status'  # new


class SearchResultsListView(ListView):  # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))


class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # Модель куда выполняется сохранение
    model = Book
    # Класс на основе которого будет валидация полей
    form_class = BookForm
    # Выведем все существующие записи на странице
    extra_context = {'books': Book.objects.all()}
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'books/create.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = '/books/create/'
    login_url = 'account_login'  # new
    permission_required = 'books.special_status'
