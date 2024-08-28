# EX9.Create function to find average of price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def average_price(products):
    total = 0
    count = len(products)
    if count == 0:
        return 0      
    for product in products:
        total += product["price"]
    average = total / count
    return average
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
result = average_price(products)
print("average of price: ",result) 