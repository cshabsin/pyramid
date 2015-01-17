import re
import util

QWERTY_RE = re.compile(r"Letters located in the (top|middle|bottom) row on a QWERTY keyboard: (.*)")
class QwertyHandler(object):
    @staticmethod
    def matches(line):
        return QWERTY_RE.match(line)

    @staticmethod
    def prune(line, words):
		location = QWERTY_RE.match(line).group(1)
		desc = QWERTY_RE.match(line).group(2)
		if location == "top":
			matchLetters = "QWERTYUIOP"
		if location == "middle":
			matchLetters = "ASDFGHJKL"
		if location == "bottom":
			matchLetters = "ZXCVBNM"
		def matchCount(word, matchLetters):
			return sum([1 for letter in word.upper() if letter in matchLetters])
		words = [word for word in words 
				 if util.value_matches(desc, matchCount(word, matchLetters), len(word))]
		return words


ALL_HANDLERS = [QwertyHandler]
