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

NONOVERLAPPING_RE = re.compile(r"If you marked nonoverlapping (.*), you could mark at most: (.*)")
class NonoverlappingHandler(object):
    @staticmethod
    def matches(line):
        return NONOVERLAPPING_RE.match(line)
        
    @staticmethod
    def prune(line, words):
        wordSetName = NONOVERLAPPING_RE.match(line).group(1)
        desc = NONOVERLAPPING_RE.match(line).group(2)
        if wordSetName == "US state postal abbreviations":
            #Open question: DC, territories?
            wordSet = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        targetLength = len(wordSet[0])
        def best(word, wordset, targetLength):
            matches = 0
            currentIndex = 0
            while (currentIndex < len(word) - targetLength + 1):
                if word[currentIndex:currentIndex + targetLength] in wordSet:
                    matches += targetLength
                    currentIndex += targetLength
                else:
                    currentIndex += 1
            
            return matches
        words = [word for word in words
                 if util.value_matches(desc, best(word.upper(), wordSet, targetLength), len(word))]
        return words
            
ALL_HANDLERS = [QwertyHandler, NonoverlappingHandler]
