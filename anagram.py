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
        for w in wordlist:
            c = AnagramDB.charcount(w)
            AnagramDB._charcounts[c].append(w)

    @staticmethod
    def hasAnagram(word):
        c = AnagramDB.charcount(word)
        return c in AnagramDB._charcounts and len(AnagramDB._charcounts[c]) > 1

    @staticmethod
    def hasAnagramPlusOne(word):
        """ has an anagram in word list when combined with one letter
        """
        c = AnagramDB.charcount(word)
        for k in AnagramDB._charcounts.iterkeys():
            diff_count = 0
            valid = True
            for i in range(26):
                if c[i] == k[i]:
                    continue
                if c[i] < k[i]:
                    valid = False
                    break
                diff_count += c[i] - k[i]
                if diff_count > 1:
                    valid = False
                    break
            if diff_count == 1:
                return True
        return False

    @staticmethod
    def hasAnagramPlusTwo(word):
        """ has an anagram in word list when combined with two letters
        """
        c = AnagramDB.charcount(word)
        for k in AnagramDB._charcounts.iterkeys():
            diff_count = 0
            valid = True
            for i in range(26):
                if c[i] == k[i]:
                    continue
                if c[i] < k[i]:
                    valid = False
                    break
                diff_count += c[i] - k[i]
                if diff_count > 2:
                    valid = False
                    break
            if diff_count == 2:
                return True
        return False
