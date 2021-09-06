import codecademylib
import pandas as pd
#Loading the data into a dataframe
inventory = pd.read_csv("inventory.csv")
print(inventory.head(10))
#Selecting rows with Staten Island location
staten_island = inventory.iloc[0:10]
print(staten_island)
#Selecting the product description column
product_request = inventory["product_description"]
print(product_request)
#Selecting all rows where location is equal to Brooklyn and product_type is equal to seeds
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
print(seed_request)
#Adding a column called in_stock which is True if quantity is greater than 0 and False if quantity equals 0
inventory["in_stock"] = inventory["quantity"].apply(lambda x: "True" if x > 0 else "False")
print(inventory)
#Adding a column called total_value that is equal to price multiplied by quantity
inventory["total_value"] = inventory.price * inventory.quantity
print(inventory) 
#Combining product_type and product_description into a single string, that is the description of each product
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
#Creating a new column called full_description that has the complete description of each product
inventory["full_description"] = inventory.apply(combine_lambda, axis = 1)
print(inventory)