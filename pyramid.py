import sys
import handlers
import anagram

with open("words.txt", "r") as wordfile:
    words = [line.strip() for line in wordfile]

anagram.AnagramDB.init(words)
    
filename = sys.argv[1]
f = open(filename, "r")
for line in f:
    line = line.strip()
    any_matched = False
    for handler in handlers.ALL_HANDLERS:
        if handler.matches(line):
            any_matched = True
            words = handler.prune(line, words)
    if not any_matched:
        print line

if len(words) > 20000:
    print "Too many: %d" % len(words)
    sys.exit(1)

print words
