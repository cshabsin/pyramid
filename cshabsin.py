import re

LENGTHRANGE_RE = re.compile(
    r"Length: between (\d*) and (\d*) \(inclusive\) letters") 
LENGTHEXACT_RE = re.compile(
    r"Length: (\d*) letters")

class LengthHandler(object):
    @staticmethod
    def matches(line):
        return LENGTHRANGE_RE.match(line) or LENGTHEXACT_RE.match(line)

    @staticmethod
    def prune(line, words):
        g = LENGTHRANGE_RE.match(line)
        if g:
            l = int(g.group(1))
            h = int(g.group(2))
        else:
            g = LENGTHEXACT_RE.match(line)
            l = int(g.group(1))
            h = int(g.group(1))
        words = [word for word in words if len(word) >= l and len(word) <= h]
        return words


STARTVOWEL_RE = re.compile(r"Starts with a vowel: (.*)")
class StartVowelHandler(object):
    @staticmethod
    def matches(line):
        return STARTVOWEL_RE.match(line)

    @staticmethod
    def prune(line, words):
        val = STARTVOWEL_RE.match(line).group(1) == "YES"
        print val
        def starts_with_vowel(word):
            return word[0].upper() in "AEIOU"
        words = [word for word in words if starts_with_vowel(word) == val]
        return words
    

ALL_HANDLERS = [LengthHandler, StartVowelHandler]
