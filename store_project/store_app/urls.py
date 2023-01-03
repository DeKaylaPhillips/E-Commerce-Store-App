from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
    path('search/<str:query_string>/', views.search, name='search'),
]