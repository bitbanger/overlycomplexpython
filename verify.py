#!/usr/bin/python

import sys

print "good" if sum([[0 if filter(lambda tr: sum(tr) == ((len(sab[0])*3 * (len(sab[0])*3 + 1))/2/len(sab[0])), sab[0]) == sab[0] else 1, 0 if (sum([0 if sab[0][i][2] + sab[0][(i + 1) % len(sab[0])][0] == sab[1][i] else 1 for i in range(len(sab[0]))]) == 0) else 1] for sab in [([map(int, tr.split('.')) for tr in sys.stdin.readline()[:-1].split(' - ')], map(int, open(sys.argv[1], 'r').readlines()[1][:-1].split(" ")))]][0]) == 0 else "bad" # Notes: I packaged up the trs and the bridges together in a 2-tuple because I needed to bind the open and readline calls once, so I stuck the results in a tuple as the single element in a list iterated over by a list comprehension, whose one-iteration variable is called "sab"; this is the closest alternative I could think of to a "let" statement
