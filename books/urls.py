

from django.urls import path
from .views import (BookListView, BookDetailView, SearchResultsListView,
                    BookCreate)  # new


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),  # new
    # path('create/', CreateWork.as_view(), name='create'),  # new когда использую класс
    path('create/', BookCreate.as_view(), name='create'),  # new
]
