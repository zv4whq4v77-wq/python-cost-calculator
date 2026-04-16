# Simple Cost Calculator

def calculate_total(price, tax_rate, discount):
    tax_amount = price * (tax_rate / 100)
    discount_amount = price * (discount / 100) 
    total = price + tax_amount - discount_amount
    return total

# Example values
price = 100
tax_rate = 8
discount = 10

total = calculate_total(price, tax_rate, discount)

print(f"Final Price: ${total:.2f}")
