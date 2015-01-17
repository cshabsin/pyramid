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
		val = QWERTY_RE.match(line).group(2)
		if location == "top":
			matchLetters = "QWERTYUIOP"
		if location == "middle":
			matchLetters = "ASDFGHJKL"
		if location == "bottom":
			matchLetters = "ZXCVBNM"
		def matchCount(word, matchLetters):
			return len([letter for letter in list(word.upper()) if (letter in matchLetters)])
		words = [word for word in words if (matchCount(word, matchLetters) == int(val))];
		return words


ALL_HANDLERS = [QwertyHandler]
