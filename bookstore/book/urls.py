from django.urls import path
from . import views
from .views import BookList, BookDetailView, SearchResultsView, BookCheckout, add_to_cart,cart
from . import views

urlpatterns = [
        path('',BookList.as_view(),name='booklist'),
        path('details/<int:pk>/',BookDetailView.as_view(),name='details'),
        path('search/', SearchResultsView.as_view(), name='search'),
        path('checkout/<int:pk>/', BookCheckout.as_view(), name='checkout'),
        path('cart/',cart,name = 'mycart'),
        path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),

]