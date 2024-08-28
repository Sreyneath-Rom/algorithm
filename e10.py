# EX10.Show product name that has maximum price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def find_max_price_product(products):
    if not products:
        return None 
    max_price_product = products[0]   
    for product in products:
        if product["price"] > max_price_product["price"]:
            max_price_product = product   
    return (max_price_product["name"], max_price_product["price"])
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
result = find_max_price_product(products)
print(result)
