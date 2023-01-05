from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .csv_parser import Csv_Parser
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
load_dotenv()

import os
import re
import json
import requests



inventory = Csv_Parser('/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/inventory.csv')
cart = Csv_Parser('/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/cart.csv')

def index(request):
    # Plain url links used on index template due to picture load bug.
    data = {
        'image_1': "https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg",
        'image_2': "https://images.pexels.com/photos/2089698/pexels-photo-2089698.jpeg",
        'image_3': "https://images.pexels.com/photos/2251247/pexels-photo-2251247.jpeg"
    } 
    return render(request, 'index.html', data)

def category(request, category_id):
    data = []

    for category in inventory.all_data:
        if int(category['category_id']) == category_id:
            data.append(category)

    return render(request, 'category.html', {'data': data})

def product(request, product_id):
    data = []

    # This loop grabs a singular product's dictionary from the inventory and renders it's information to the page.
    for product in inventory.all_data:
        
        if int(product['product_id']) == product_id:
            data.append(product)

    return render(request, 'product.html', {'data': data})

@csrf_exempt
def update_cart(request, product_id):
    # This loop checks to see if the product being added to the cart is currently in the cart.
    for product in cart.all_data:
        
        if int(product['product_id']) == product_id: # Check to see if a product in the cart matches the requested item to add to the cart.
            initial_price = float(product['cost'])/int(product['quantity']) # Initial price is the current item cost value divided by the current quantity value.            
            product['quantity'] = int(product['quantity']) + 1 # The quantity of the item is to be increased by 1 when adding to the cart.
            product['cost'] = "{:.2f}".format(initial_price * product['quantity']) # The updated cost of the item will be the current inital cost times the new quantity in the cart.
            cart.append_dictionaries(all_rows=cart.all_data) # Updates CSV file by passing in all of the updated cart data.
            return JsonResponse({"Success": True, "data": product})
    
    # This loop is used if the requested item to add to the cart is not currently in the cart.
    for product in inventory.all_data: 

        if int(product['product_id']) == product_id: # Find the specific item to add by checking if an item in the inventory matches the requested item to add.
            product['quantity'] = 1 # When found, set the quantity of the product equal to 1 because it is a new addition to the cart.
            cart.append_dictionary(dict=product) # Updates CSV file by passing in the new product dictionary to add which will be appended to the cart.
            return JsonResponse({"Success": True, "data": product})

    return JsonResponse({"Success": False, "data": "Cart not updated."})

def shopping_cart(request):
    total_cost = 0

    # This loop calculates and formats the total cost based on the items in the cart to be rendered to the page.
    for product in cart.all_data:
        product['cost'] = float(product['cost']) # Converting product cost from string to float for calculation of total.
        total_cost += product['cost'] # Adds each item in the cart to calculate the total cost.
        product['cost'] = "{:.2f}".format(product['cost']) # Format product cost back to a string currency value instead of a float.
    total_cost = "${:.2f}".format(total_cost) # Format new total cost to a currency value.

    data = {'total': total_cost, 'cart': cart.all_data}
            
    return render(request, 'cart.html', data)

@csrf_exempt 
def remove_cart_item(request):
    data = json.loads(request.body) # Converts the request bytes to json formatting to extract and manipulate the data.
    
    # This loop finds the item to be removed in the cart, and deletes to requested item from the CSV file.
    for product in cart.all_data:
        if int(product['product_id']) == data['product_id']:
            cart.delete_dictionary(dict=product)
            return JsonResponse({"Success": True, "data": "Item removed from cart."})
    return JsonResponse({"Success": False, "data": "Item not removed"})

@csrf_exempt
def search(request):
    print("Search page works.")
    query = request.POST.get("query")
    
    inv = {'data': inventory.all_data}
    found = [x for x in inv['data'] if query in x['name'].lower()]
    
    if found:
        for product in found:
            data = {
                'item': product['name'],
                'image': product['image_url']
            }
    else:
        # API calls to be made for search queries that do not match a current product in the inventory
        not_found = True
        api_auth = OAuth1(os.environ['API_KEY'], os.environ['SECRET_KEY'])
        api_endpoint = f"http://api.thenounproject.com/icon/{query}"
        response = requests.get(api_endpoint, auth=api_auth) 
        obj = json.loads(response.content) # Convert bytes to parsible json object
        image_url = obj['icon']['preview_url'] # Access to image URL based on search query.
        if not_found:
            data = {
                'item': "SORRY - WE'RE OUT OF STOCK :(",
                'image': image_url
            }
    return render(request, 'search-results.html', data)
    # return HttpResponse(f"Search page with query..'{query}' -- {item}")
