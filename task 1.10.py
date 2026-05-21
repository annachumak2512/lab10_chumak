def reverse_number(n):
    if n < 10:
        return n
    last_digit = n % 10
    remaining = n // 10
    from math import log10
    num_digits_remaining = int(log10(remaining)) + 1
    return last_digit * (10 ** num_digits_remaining) + reverse_number(remaining)
print(reverse_number(1234))  
print(reverse_number(5))