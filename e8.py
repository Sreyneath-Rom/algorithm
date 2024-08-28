# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum_total_price(products):
    total = 0
    for product in products:
        total += product["price"]
    return total
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
result = sum_total_price(products)
print("sum total of price ",result)  
