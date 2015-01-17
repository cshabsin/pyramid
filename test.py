import brianh
import cshabsin
import util

print util.sum_of_letters_a1("undertrained")

print cshabsin.SumLetterHandler.prune("Sum of letters (A=1, B=2, etc) is divisible by 7: YES", ["undertrained"])

print brianh.best("matinees".upper(), brianh.WORD_SETS["chemical element symbols (atomic number 112 or below)"])
print brianh.best("quibbles".upper(), brianh.WORD_SETS["chemical element symbols (atomic number 112 or below)"])
print brianh.best("wobblies".upper(), brianh.WORD_SETS["chemical element symbols (atomic number 112 or below)"])
