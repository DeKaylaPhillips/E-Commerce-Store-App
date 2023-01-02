from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pprint as pp
import json
import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
load_dotenv()
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

    # API calls to be made for search queries that do not match a current product in the inventory
    api_auth = OAuth1(os.environ['API_KEY'], os.environ['SECRET_KEY'])
    api_endpoint = f"http://api.thenounproject.com/icon/{query_string}"
    response = requests.get(api_endpoint, auth=api_auth) 
    data = json.loads(response.content) # Convert bytes to parsible json object
    out_of_stock_image = data['icon']['preview_url'] # Access to image URL based on search query.
    
    return HttpResponse(f"Search page with query for {query_string}.")
