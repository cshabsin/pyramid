import re
import cshabsin
import jtwang
import brianh
import caesar
import util

SCRABBLE_RE = re.compile(r"Base Scrabble score: (.*)")
SCRABBLE_VALS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
                 5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
                 1, 4, 4, 8, 4, 10]
class ScrabbleHandler(object):
    @staticmethod
    def matches(line):
        return SCRABBLE_RE.match(line)

    @staticmethod
    def prune(line, words):
        desc = SCRABBLE_RE.match(line).group(1)
        def scrabble_score(word):
            return sum([SCRABBLE_VALS[ord(c.upper())-65] for c in word])
        words = [word for word in words if util.value_matches(desc, scrabble_score(word), 
                                                              len(word))]
        return words


CONTAINS_RE = re.compile(r"Contains: (.*)")
class ContainsHandler(object):
    @staticmethod
    def matches(line):
        return CONTAINS_RE.match(line)

    @staticmethod
    def prune(line, words):
        val = CONTAINS_RE.match(line).group(1)
        words = [word for word in words if val in word.upper()]
        return words

from collections import defaultdict
ALL_HANDLERS = defaultdict(list)
ALL_HANDLERS[1] = [ContainsHandler]
ALL_HANDLERS[10] = [ScrabbleHandler]
ALL_HANDLERS[30] = [caesar.CaesarHandler]
for d in (cshabsin.ALL_HANDLERS, jtwang.ALL_HANDLERS, brianh.ALL_HANDLERS):
    for (priority, handlers) in d.iteritems():
        ALL_HANDLERS[priority].extend(handlers)

# no properties implemented yet
import properties
ALL_HANDLERS[200].append(properties.PropertyHandler)
