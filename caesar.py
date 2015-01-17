import re
from collections import defaultdict

CAESAR_RE = re.compile(r"Can be Caesar shifted to produce another word in the word list: (\w+)")
class CaesarHandler(object):
    _caesars = defaultdict(int)

    @staticmethod
    def wordToDiff(word):
        diffs = [ord(word[i+1]) - ord(word[i]) for i in xrange(len(word)-1)]
        for i in xrange(len(diffs)):
            if diffs[i] < 0:
                diffs[i] += 26
        return tuple(diffs)
    
    @staticmethod
    def init(wordlist):
        if len(CaesarHandler._caesars) > 0:
            return
        for w in wordlist:
            diff = CaesarHandler.wordToDiff(w)
            CaesarHandler._caesars[diff] += 1

    @staticmethod
    def matches(rule):
        return CAESAR_RE.match(rule)

    @staticmethod
    def prune(rule, words):
        m = CAESAR_RE.match(rule)
        truth = m.group(1) == 'YES'

        return [w for w in words if CaesarHandler._caesars.get(CaesarHandler.wordToDiff(w), 0) > 1]
            
