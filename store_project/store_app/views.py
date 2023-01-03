from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pprint as pp
import json
import csv
import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
load_dotenv()
from .csv_parser import Csv_Parser

products = Csv_Parser()

def index(request):
    # Plain url links used on index template due to picture load bug.
    data = {
        'image_1': "https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg",
        'image_2': "https://images.pexels.com/photos/2089698/pexels-photo-2089698.jpeg",
        'image_3': "https://images.pexels.com/photos/2251247/pexels-photo-2251247.jpeg"
    } 
    return render(request, 'index.html', data)

def category(request, category_id):
    all_products = products.all_inventory() 
    data = []

    for category in all_products:
        if int(category['category_id']) == category_id:
            data.append({
                'category': category['category'],
                'id': category['product_id'],
                'name': category['name'],
                'cost': category['cost'],
                'image_url': category['image_url']  
            })
    return render(request, 'category.html', {'data': data})

def product(request, product_id):
    print("Product page works.")
    all_products = products.all_inventory()
    data = []

    for product in all_products:
        if int(product['product_id']) == product_id:
            data.append({
                'id': product['product_id'],
                'name': product['name'],
                'cost': product['cost'],
                'image_url': product['image_url'] 
            })
    return render(request, 'product.html', {'data': data})

@csrf_exempt
def shopping_cart(request):
    print("Shopping cart page works.")
    all_products = products.all_inventory()
    cart = products.shopping_cart_details()
    cart_list = []
    
    if request.method == "POST":
        for key, value in request.POST.items():
            item_id = value

        for item in all_products:
            if int(item['product_id']) == int(item_id):
                product_id = item['product_id']
                name = item['name']
                cost = item['cost']
                image_url = item['image_url']
            
        for item in cart:
            print(item)
            if item['product_id'] == product_id:
                print('Item already exists')
                item['quantity'] = int(item['quantity']) + 1     
            else: 
                with open('/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/cart.csv', 'a', newline='') as cart_file: 
                    fieldnames = ['product_id', 'name', 'cost', 'quantity', 'image_url']
                    writer = csv.DictWriter(cart_file, fieldnames=fieldnames)
                        
                    added_item = {
                        'product_id': product_id,
                        'name': name,
                        'cost': cost,
                        'image_url': image_url,
                        'quantity': int(item['quantity']) + 1
                    }
                    
                writer.writerow(added_item)
                print(added_item)

    if request.method == "GET":
        for items in cart:
            cart_list.append(items)
    print(cart_list)

    return render(request, 'cart.html', {'data': cart_list})

def search(request, query_string):
    print("Search page works.")
    print(request.data['query_string'])
    # print(query_string)
    # API calls to be made for search queries that do not match a current product in the inventory
    api_auth = OAuth1(os.environ['API_KEY'], os.environ['SECRET_KEY'])
    api_endpoint = f"http://api.thenounproject.com/icon/{query_string}"
    response = requests.get(api_endpoint, auth=api_auth) 
    data = json.loads(response.content) # Convert bytes to parsible json object
    out_of_stock_image = data['icon']['preview_url'] # Access to image URL based on search query.
    
    return HttpResponse(f"Search page with query for {query_string}.")
