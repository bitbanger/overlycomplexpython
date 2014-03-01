#!/usr/bin/python

import sys

print "good" if sum([[0 if filter(lambda triad: sum(triad) == ((len(sol_and_bridges[0])*3 * (len(sol_and_bridges[0])*3 + 1))/2/len(sol_and_bridges[0])), sol_and_bridges[0]) == sol_and_bridges[0] else 1, 0 if (sum([0 if sol_and_bridges[0][i][2] + sol_and_bridges[0][(i + 1) % len(sol_and_bridges[0])][0] == sol_and_bridges[1][i] else 1 for i in range(len(sol_and_bridges[0]))]) == 0) else 1] for sol_and_bridges in [([map(int, triad.split('.')) for triad in sys.stdin.readline()[:-1].split(' - ')], map(int, open(sys.argv[1], 'r').readlines()[1][:-1].split(" ")))]][0]) == 0 else "bad" # Notes: I packaged up the triads and the bridges together in a 2-tuple because I needed to bind the open and readline calls once, so I stuck the results in a tuple as the single element in a list iterated over by a list comprehension, whose one-iteration variable is called sol_and_bridges; this is the closest alternative I could think of to a "let" statement
