is_palindrome = lambda s: (clean_s := s.lower().replace(" ", "")) == clean_s[::-1]
print(is_palindrome("Anna"))
print(is_palindrome("Python"))                    