def sum_of_letters_a1(word):
    return sum([ord(c.upper())-64 for c in word])
