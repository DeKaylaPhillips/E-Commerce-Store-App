from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    print("Homepage works.")
    return HttpResponse("HomePage")

def category(request, category_id):
    print("Category page works.")
    return HttpResponse(f"Category page for category with the ID number {category_id}.")

def product(request, product_id):
    print("Product page works.")
    return HttpResponse(f"Product page for product with the ID number {product_id}.")

def shopping_cart(request):
    print("Shopping cart page works.")
    return HttpResponse("Shopping cart page.")

def search(request, query_string):
    print("Search page works.")
    return HttpResponse(f"Search page with query for {query_string}.")