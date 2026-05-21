filter_words = lambda words: list(filter(lambda w: len(w) > 4, words))

print(filter_words(["cat", "elephant", "dog", "house", "algorithm"]))
print(filter_words(["I", "am"]))
