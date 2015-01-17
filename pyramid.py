import sys
import handlers

with open("words.txt", "r") as wordfile:
    words = [line.strip() for line in wordfile]

filename = sys.argv[1]
f = open(filename, "r")
for line in f:
    line = line.strip()
    for handler in handlers.ALL_HANDLERS:
        if handler.matches(line):
            words = handler.prune(line, words)

if len(words) > 20000:
    print "Too many: %d" % len(words)
    sys.exit(1)

print words
