def flexible_average(*args):
    valid_numbers = [x for x in args if isinstance(x, (int, float))]
    if not valid_numbers:
        return None
    return sum(valid_numbers) / len(valid_numbers)

print(flexible_average(10, 20, 30))
print(flexible_average(5))
print(flexible_average())  
