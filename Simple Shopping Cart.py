# Simple Shopping Cart

# Take customer's name
customer_name = input("Enter customer's name: ")

# Take names and prices of 3 products
product1 = input("Enter name of Product 1: ")
price1 = float(input("Enter price of Product 1: "))

product2 = input("Enter name of Product 2: ")
price2 = float(input("Enter price of Product 2: "))

product3 = input("Enter name of Product 3: ")
price3 = float(input("Enter price of Product 3: "))

# Calculate subtotal
subtotal = price1 + price2 + price3

# Determine discount
if subtotal >= 5000:
    discount_rate = 20
elif subtotal >= 3000:
    discount_rate = 10
elif subtotal >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

# Calculate discount amount
discount = subtotal * discount_rate / 100

# Calculate final total
final_total = subtotal - discount

# Display shopping summary using f-string
print("--- Shopping Summary ---")
print(f"Customer Name: {customer_name}")
print(f"Product 1: {product1} - {price1:.2f}")
print(f"Product 2: {product2} - {price2:.2f}")
print(f"Product 3: {product3} - {price3:.2f}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f} ({discount_rate}%)")
print(f"Final Total: {final_total:.2f}")
