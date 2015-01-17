import sys
import handlers
import anagram
import caesar

__WORDS = []
with open("words.txt", "r") as wordfile:
    __WORDS = [line.strip() for line in wordfile]

def runPyramid(filename):
    words = __WORDS
    with open(filename, 'r') as rulefile:
        rules = [line.strip() for line in rulefile]

    for (priority, handler_list) in sorted(handlers.ALL_HANDLERS.items()):
        # try each handler on the rules
        for h in handler_list:
            delInx = []
            for inx in xrange(len(rules)):
                rule = rules[inx]
                if h.matches(rule):
                    words = h.prune(rule, words)
                    delInx.append(inx)
            for i in sorted(delInx, reverse=True):
                del rules[i]

    for r in rules:
        print r

    if len(words) > 20000:
        print "Too many: %d" % len(words)
    else:
        print words

anagram.AnagramDB.init(__WORDS)
caesar.CaesarHandler.init(__WORDS)

for filename in sys.argv[1:]:
    print "=== %s ===" % filename
    runPyramid(filename)

