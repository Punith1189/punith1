from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('bill/', views.bill, name='bill'),
   path('confirm-payment/', views.confirm_payment, name='confirm_payment'),
   path('payment-success/', views.payment_success, name='payment_success'),
   path('view_cart/', views.view_cart, name='view_cart'),
   
   
]
