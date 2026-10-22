def calculate_bill(price, quantity):
    bill = price * quantity
    if bill > 2000:
        discount = bill * 0.10  # 10% discount
        bill = bill - discount
    return bill
print(calculate_bill(500, 5))