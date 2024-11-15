X = int(input())
discount_10 = 0.10 * X
discount_flat = 100
max_discount = max(discount_10, discount_flat)
amount_to_pay = X - max_discount
print(int(amount_to_pay))
