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

ALL_HANDLERS = [LengthHandler]
