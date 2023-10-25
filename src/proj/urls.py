from django.contrib import admin
from django.urls import path
from book_shop import views
from django.views.generic import DetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_shop/currency/<int:pk>/', views.CurrencyDetail.as_view()),
    path('book_shop/currency/', views.CurrencyList.as_view()),
    path('book_shop/currency/create/', views.CurrencyCreate.as_view()),
    path('book_shop/currency/update/<int:pk>/', views.CurrencyUpdate.as_view()),
    path('book_shop/order/<int:pk>/', views.OrderDetail.as_view()),
    path('book_shop/order/', views.OrderList.as_view()),
    path('book_shop/order/create/', views.OrderCreate.as_view()),
    path('book_shop/order/update/<int:pk>/', views.OrderUpdate.as_view()),
    path('book_shop/order/delete/<int:pk>/', views.OrderDelete.as_view()),
    path('book_shop/currency/delete/<int:pk>/', views.CurrencyDelete.as_view()),
]
