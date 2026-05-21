discount_prices = lambda prices: list(map(lambda p: round(p * 0.85, 2), prices))
print(discount_prices([100, 200, 300, 400]))
print(discount_prices([50, 150]))
