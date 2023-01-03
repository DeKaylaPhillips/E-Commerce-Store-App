import csv
import pprint as pp
import json


class Csv_Parser:

    def __init__(self):
        pass

    def all_inventory(self):
        data = []

        with open('/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/inventory.csv', 'r', newline='') as inv_file:
            reader = csv.DictReader(inv_file)

            for row in reader:
                data.append(row)
         
        return data

    def shopping_cart_details(self):
        data = []

        with open('/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/cart.csv', 'r') as cart:
            reader = csv.DictReader(cart)
            
            for row in reader:
                data.append(row)

        return data
            