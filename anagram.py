import numpy as np
from collections import Counter, defaultdict

class AnagramDB(object):
    """ Contains count of characters of each word in wordlist, to be
    used for anagramming. charcounts goes from character counts to list of words
    with that character count. Character counts are represented as length 26 tuples """
    _charcounts = defaultdict(list)
    
    @staticmethod
    def charcount(word):
        c = Counter(word.upper())
        return tuple([c[l] for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])

    @staticmethod
    def init(wordlist):
        if len(AnagramDB._charcounts) > 0:
            return
        for w in wordlist:
            c = AnagramDB.charcount(w)
            AnagramDB._charcounts[c].append(w)
        AnagramDB._charmatrix = np.matrix(AnagramDB._charcounts.keys())

    @staticmethod
    def hasAnagram(word):
        c = AnagramDB.charcount(word)
        return c in AnagramDB._charcounts and len(AnagramDB._charcounts[c]) > 1

    @staticmethod
    def hasAnagramPlusOne(word):
        """ has an anagram in word list when combined with one letter
        """
        c = AnagramDB.charcount(word)
        ref = np.array(c)
        mDiff = AnagramDB._charmatrix - ref
        gt = np.all(mDiff >= 0, 1)
        sm = np.sum(mDiff, 1) == 1
        return np.any(gt & sm)

    @staticmethod
    def hasAnagramPlusTwo(word):
        """ has an anagram in word list when combined with two letters
        """
        c = AnagramDB.charcount(word)
        ref = np.array(c)
        mDiff = AnagramDB._charmatrix - ref
        gt = np.all(mDiff >= 0, 1)
        sm = np.sum(mDiff, 1) == 2
        return np.any(gt & sm)
