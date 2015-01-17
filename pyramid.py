import sys
import handlers
import anagram

with open("words.txt", "r") as wordfile:
    words = [line.strip() for line in wordfile]

anagram.AnagramDB.init(words)

filename = sys.argv[1]
with open(filename, 'r') as rulefile:
    rules = [line.strip() for line in rulefile]

for (priority, handlers) in sorted(handlers.ALL_HANDLERS.items()):
    # try each handler on the rules
    for h in handlers:
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
    sys.exit(1)

print words
