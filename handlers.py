import re

scrabble_re = re.compile(r"Base Scrabble score: (\d*) points")
SCRABBLE_VALS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
                 5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
                 1, 4, 4, 8, 4, 10]
class ScrabbleHandler(object):
    @staticmethod
    def matches(line):
        return scrabble_re.match(line)

    @staticmethod
    def prune(line, words):
        score = int(scrabble_re.match(line).group(1))
        def scrabble_score(word):
            return sum([SCRABBLE_VALS[ord(c.upper())-65] for c in word])
        words = [word for word in words if scrabble_score(word) == score]
        return words

ALL_HANDLERS = [ScrabbleHandler]
