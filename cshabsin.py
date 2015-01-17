import re
import util

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
        def starts_with_vowel(word):
            return word[0].upper() in "AEIOU"
        words = [word for word in words if starts_with_vowel(word) == val]
        return words


VOWEL_RE = re.compile(r"Vowels: (.*)")
class VowelHandler(object):
    @staticmethod
    def matches(line):
        return VOWEL_RE.match(line)

    @staticmethod
    def prune(line, words):
        desc = VOWEL_RE.match(line).group(1)
        def num_vowels(word):
            return sum([1 for c in word if c.upper() in "AEIOU"])
        words = [word for word in words
                 if util.value_matches(desc, num_vowels(word), len(word))]
        return words


SUMLETTERDIV_RE = re.compile(
    r"Sum of letters \(A=1, B=2, etc\) is divisible by (\d*): (.*)")
SUMLETTER_RE = re.compile(
    r"Sum of letters \(A=1, B=2, etc\): (.*)")
class SumLetterHandler(object):
    @staticmethod
    def matches(line):
        return (
            SUMLETTERDIV_RE.match(line) or SUMLETTER_RE.match(line))

    @staticmethod
    def prune(line, words):
        m = SUMLETTERDIV_RE.match(line)
        if m:
            modulo = int(m.group(1))
            is_divisible = m.group(2) == "YES"
            words = [word for word in words
                     if (util.sum_of_letters_a1(word)%modulo == 0) == is_divisible]
            return words

        m = SUMLETTER_RE.match(line)
        if m:
            words = [word for word in words
                     if util.value_matches(
                             m.group(1), util.sum_of_letters_a1(word), len(word))]
            return words

        raise Exception("Whoa")
                     

ENDSWITH_RE = re.compile(r"Ends with: (.*)")
class EndsWithHandler(object):
    @staticmethod
    def matches(line):
        return ENDSWITH_RE.match(line)

    @staticmethod
    def prune(line, words):
        val = ENDSWITH_RE.match(line).group(1)
        words = [word for word in words if word.upper().endswith(val)]
        return words


DOUBLED_LETTER_RE = re.compile(r"Contains at least one doubled letter: (.*)")
class DoubledLetterHandler(object):
    @staticmethod
    def matches(line):
        return DOUBLED_LETTER_RE.match(line)

    @staticmethod
    def prune(line, words):
        want_has_double = DOUBLED_LETTER_RE.match(line).group(1) == "YES"
        def has_double(word):
            for code in range(65, 65+26):
                if chr(code)+chr(code) in word.upper():
                    return True
            return False
        words = [word for word in words if has_double(word) == want_has_double]
        return words


ALL_HANDLERS = [LengthHandler, StartVowelHandler, SumLetterHandler, EndsWithHandler,
                VowelHandler, DoubledLetterHandler]
