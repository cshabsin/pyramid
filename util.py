import re
import string

def sum_of_letters_a1(word):
    return sum([ord(c.upper())-64 for c in word])

def base26(word):
    word = word.upper()
    table = string.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789ABCDEFGHIJKLMNOP")
    return int(word.translate(table), 26)
