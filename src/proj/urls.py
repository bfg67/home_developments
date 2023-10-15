from django.contrib import admin
from django.urls import path
from book_shop import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_shop/currency/<int:pk>/', views.currency_detail),
    path('book_shop/currency/', views.currency_list),
    path('book_shop/currency/create/', views.currency_create),
    path('book_shop/currency/update/<int:pk>/', views.currency_update),
    path('book_shop/order/<int:pk>/', views.order_detail),
    path('book_shop/order/', views.order_list),
    path('book_shop/order/create/', views.order_create),
    path('book_shop/order/update/<int:pk>/', views.order_update),
]
