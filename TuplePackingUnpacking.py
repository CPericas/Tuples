#Task 1: Customer Order Processing
#Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement:
#You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, 
# and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

#Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Chris", "TV", 1)
]
for name, item, quantity in orders:
    print(f"Name: {name} - Item: {item} - Quantity: {quantity}")