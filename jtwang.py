import anagram
import re
import util

SHA1_RE = re.compile(r"SHA-1 hash of lowercased word, expressed in hexadecimal, (contains|starts with|ends with): (\S+)")
class SHA1Handler(object):
    @staticmethod
    def matches(rule):
        return SHA1_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = SHA1_RE.match(rule)
        sha1 = m.group(2)
        sha1 = sha1.lower()

        import hashlib
        if m.group(1) == "contains":
            return [word for word in words if hashlib.sha1(word.lower()).hexdigest().find(sha1) != -1]
        elif m.group(1) == "starts with":
            return [w for w in words if hashlib.sha1(w.lower()).hexdigest().startswith(sha1)]
        elif m.group(1) == "ends with":
            return [w for w in words if hashlib.sha1(w.lower()).hexdigest().endswith(sha1)]

B26DIV_RE = re.compile(r"Word interpreted as a base 26 number \(A=0, B=1, etc\) is divisible by (\d): (\w+)")
class B26DivisibleHandler(object):
    @staticmethod
    def matches(rule):
        return B26DIV_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = B26DIV_RE.match(rule)
        truth = m.group(2) == "YES"
        div = int(m.group(1))
        words = [word for word in words if (util.base26(word) % div == 0) is truth]
        return words

B26FLOAT_RE = re.compile(r"Word interpreted as a base 26 number \(A=0, B=1, etc\) is exactly representable in IEEE 754 (single|double)-precision floating point format: (\w+)")
class B26FloatHandler(object):
    @staticmethod
    def matches(rule):
        return B26FLOAT_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = B26FLOAT_RE.match(rule)
        truth = m.group(2) == "YES"
        import numpy

        if m.group(1) == "double":
            nfunc = numpy.float64
        elif m.group(1) == "single":
            nfunc = numpy.float32

        ret = []
        for w in words:
            b26 = util.base26(w)
            if nfunc(b26) == b26:
                ret.append(w)
        return ret
        
B26INT_RE = re.compile(r"Word interpreted as a base 26 number \(A=0, B=1, etc\) is representable as an unsigned 32-bit integer: (\w+)")
class B26IntHandler(object):
    @staticmethod
    def matches(rule):
        return B26INT_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = B26INT_RE.match(rule)
        truth = m.group(1) == "YES"

        return [w for w in words if util.base26(w) <= 2**32-1]

DISTINCT_RE = re.compile(r"Distinct (consonants|vowels): (\d+)")
class DistinctHandler(object):
    vowels = set(['a','e','i','o','u'])

    @staticmethod
    def matches(rule):
        return DISTINCT_RE.match(rule)

    @staticmethod
    def distinct_consonants(word):
        return set([c for c in word.lower() if c not in DistinctHandler.vowels])

    @staticmethod
    def distinct_vowels(word):
        return set([c for c in word.lower() if c in DistinctHandler.vowels])
    
    @staticmethod
    def prune(rule, words):
        m = DISTINCT_RE.match(rule)
        count = int(m.group(2))
        if m.group(1) == "consonants":
            return [w for w in words if len(DistinctHandler.distinct_consonants(w)) == count]
        elif m.group(1) == "vowels":
            return [w for w in words if len(DistinctHandler.distinct_vowels(w)) == count]

ANAGRAM_RE = re.compile(r"Has at least one anagram that is also in the word list: (\w+)")
class AnagramHandler(object):
    @staticmethod
    def matches(rule):
        return ANAGRAM_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = ANAGRAM_RE.match(rule)
        if m.group(1) == "YES":
            truth = True
        else:
            truth = False
        return [w for w in words if anagram.AnagramDB.hasAnagram(w) is truth]
        
ANAGRAM_FUZZ_RE = re.compile(r"Can be combined with (one|two) additional (letter|letters) to produce an anagram of something in the word list: (\w+)")
class AnagramFuzzHandler(object):
    @staticmethod
    def matches(rule):
        return ANAGRAM_FUZZ_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = ANAGRAM_FUZZ_RE.match(rule)
        if m.group(3) == "YES":
            truth = True
        else:
            truth = False

        if m.group(1) == "one":
            return [w for w in words if anagram.AnagramDB.hasAnagramPlusOne(w) == truth]
        elif m.group(1) == "two":
            return [w for w in words if anagram.AnagramDB.hasAnagramPlusTwo(w) == truth]
        
if __name__ == "main":
    print "foo"

ALL_HANDLERS = {
    2: [SHA1Handler],
    3: [B26DivisibleHandler, B26FloatHandler, B26IntHandler],
    4: [DistinctHandler],
    100: [AnagramHandler, AnagramFuzzHandler]
    }

