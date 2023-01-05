import csv
import pprint as pp
import json
import os

# inventory_file = '/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/inventory.csv'
# cart_file = '/Users/dekaylaphillips/Assessments/Assessment3Retake-DeKaylaPhillips/store_project/store_app/data/cart.csv'
class Csv_Parser:

    def __init__(self, file):
        with open(os.path.join(file), 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True, delimiter=',') 
            self.column_names = reader.fieldnames
        self.file = file
        self.all_data = self.update_list()

    def update_list(self):
        data = []
        with open(self.file, 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True, delimiter=',')
            for row in reader:
                data.append(row)
        return data

    def append_dictionary(self, dict):
        with open(self.file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.column_names)
            writer.writerow(dict)
        self.all_data = self.update_list()
        return self.all_data

    def append_dictionaries(self, all_rows):
        with open(self.file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.column_names)
            writer.writeheader()
            writer.writerows(all_rows)
        self.all_data = self.update_list()
        return self.all_data

    def delete_dictionary(self, dict):
        self.all_data.remove(dict)
        self.append_dictionaries(self.all_data)
        self.all_data = self.update_list()
        return self.all_data
    
    # def all_inventory(self):
    #     data = []
    #     with open(inventory_file, 'r', newline='') as inv_file:
    #         reader = csv.DictReader(inv_file)
    #         for row in reader:
    #             data.append(row)
    #     return data
    
    # def shopping_cart_details(self):
    #     data = []

    #     with open(cart_file, 'r') as cart:
    #         reader = csv.DictReader(cart)
    #         self.column_names = reader.fieldnames
    #         for row in reader:
    #             data.append(row)
    #     return data

    # # function works! do not change!!!
    # def add_to_cart(self, product_dict): # method accepts a dictionary of information on the item passed as an argument in the views
    #     try: # can remove try/except block later for cleanup
    #         fieldnames=['product_id', 'name', 'cost', 'quantity', 'image_url']
    #         with open(cart_file, 'a', newline='') as c:
    #             writer = csv.DictWriter(c, fieldnames=fieldnames)
    #             writer.writerow(product_dict)
            
    #         self.all_data = self.shopping_cart_details()
    #         print('FROM CSV_PARSER: Check if item added to cart.')
    #         print(f"new cart data: {self.all_data}")
    #         return self.all_data

    #     except Exception as e:
    #         print(f"Error: {str(e)}")

    # def append_row(self, dict):
    #     with open(cart_file, 'a', newline='') as f:
    #         fieldnames=['product_id', 'name', 'cost', 'quantity', 'image_url']
    #         writer = csv.DictWriter(f, fieldnames=fieldnames)
    #         writer.writerow(dict)
    #     self.all_data = 
    # # def update_cart(self, product_id, quantity, cost):
    # #     try:
    # #         rows = []
    # #         with open(cart_file, 'r', newline='') as c:
    # #             reader = csv.DictReader(c)
    # #             for row in reader:
    # #                 rows.append(row)

    # #             for row in rows:
    # #                 if row['product_id'] == product_id:
    # #                     row['quantity'] = int(row['quantity']) + 1
    # #                     row['cost'] = float(row['cost'])
    # #                     row['cost'] = "{:.2f}".format(float(row['cost'] * row['quantity']))
    # #                     print(f"FROM CSV PARSER updated csv: {row}")  

    # #         with open(cart_file, 'w', newline='') as c:
    # #             fieldnames=['product_id', 'name', 'cost', 'quantity', 'image_url']
    # #             writer = csv.DictWriter(c, fieldnames=fieldnames)
    # #             writer.writeheader() 
    # #             print(f"in the writer: --- {row}")
    # #             writer.writerows(rows)   
    # #         print(f"FROM CSV PARSER all data: {rows}")
                    
    #     # except Exception as e:
    #     #     print(f"Error: {str(e)}")
