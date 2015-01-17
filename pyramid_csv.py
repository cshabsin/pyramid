import os
import glob
import sys

import handlers
import anagram
import caesar

def GetSafe(arr, row, col):
    try:
        return arr[row][col]
    except:
        return ""

def PutSafe(arr, row, col, val):
    while row >= len(arr):
        arr.append([])
    while col >= len(arr[row]):
        arr[row].append("")
    arr[row][col] = val

    
previous = []
with open("previous.csv", "r") as prevfile:
    for line in prevfile:
        previous.append(line.strip().split(","))
#with open("previous2.csv", "r") as prevfile:
#    rownum = 0
#    for line in prevfile:
#        colnum = 0
#        for entry in line.strip().split(","):
#            if not GetSafe(previous, rownum, colnum) and entry:
#                PutSafe(previous, rownum, colnum, entry)
#            colnum += 1
#        rownum += 1

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
    output.write(output_str)

total = 0
found = 0
for rownum in xrange(125):
  for colnum in xrange(142):
    filename = "row%d/row%d_col%d.txt" % (rownum, rownum, colnum)
    if not os.path.exists(filename):
        emit(",")
        continue
    total += 1
    sys.stderr.write("(%d, %d)     \r" % (rownum, colnum))
    if GetSafe(previous, rownum, colnum):
        emit(GetSafe(previous, rownum, colnum) + ",")
        found += 1
        continue
    words = all_words[:]
    with open(filename, "r") as f:
        rules = [line.strip() for line in f]
        for (priority, handler_list) in sorted(handlers.ALL_HANDLERS.items()):
            for h in handler_list:
                if not words: break
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
            found += 1
        else:
            if not words:
                sys.stderr.write("No words found at (%d, %d)\n" % (rownum, colnum))
            emit(",")
  emit("\n")

print "Found %d of %d entries." % (found, total)
