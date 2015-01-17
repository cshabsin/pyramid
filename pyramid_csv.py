import os
import glob
import sys

import handlers
import anagram
import caesar

with open("words.txt", "r") as wordfile:
    all_words = [line.strip() for line in wordfile]

anagram.AnagramDB.init(all_words)
caesar.CaesarHandler.init(all_words)

def sorted_glob():
    for rownum in xrange(125):
        for colnum in xrange(142):
            yield "row%d/row%d_col%d.txt" % (rownum, rownum, colnum)

output = open("output.csv", "w")
            
def emit(output_str):
    sys.stdout.write(output_str)
    output.write(output_str)
            
for rownum in xrange(125):
  for colnum in xrange(142):
    filename = "row%d/row%d_col%d.txt" % (rownum, rownum, colnum)
    if not os.path.exists(filename):
        emit(",")
        continue
    words = all_words[:]
    with open(filename, "r") as f:
        rules = [line.strip() for line in f]
        for (priority, handler_list) in sorted(handlers.ALL_HANDLERS.items()):
            for h in handler_list:
                delInx = []
                for inx in xrange(len(rules)):
                    rule = rules[inx]
                    if h.matches(rule):
                        words = h.prune(rule, words)
                        delInx.append(inx)
                for i in sorted(delInx, reverse=True):
                    del rules[i]

        if len(words) == 1:
            emit(words[0].upper() + ",")
        else:
            emit(",")
  emit("\n")
