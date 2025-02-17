balance = 50
item_price = 15
tax_perc = 3
total_cost = item_price + (item_price * tax_perc / 100)
left_money = balance - total_cost
print(left_money)