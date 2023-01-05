from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update-cart'),
    path('remove-cart-item/', views.remove_cart_item, name='remove-cart-item'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
    path('search/', views.search, name='search'),
]