#-----------------------------------------------------------------------
# transition.py
#-----------------------------------------------------------------------

import stdio
import stdarray

# Read links from standard input and write the corresponding
# transition matrix to standard output. First, process the input
# to count the outlinks from each page. Then apply the 90-10 rule to
# compute the transition matrix. Assume that there are no pages that
# have no outlinks in the input.

n = stdio.read_int()

linkCounts = stdarray.create_2d(n, n, 0)
outDegrees = stdarray.create_1d(n, 0)

while not stdio.is_empty():
    # Accumulate link counts.
    i = stdio.read_int()
    j = stdio.read_int()
    outDegrees[i] += 1
    linkCounts[i][j] += 1

stdio.writeln(str(n) + ' ' + str(n))

for i in range(n):
    # Print probability distribution for row i.
    for j in range(n):
        # Print probability for column j.
        p = (.90 * linkCounts[i][j] / outDegrees[i]) + (.10 / n)
        stdio.writef('%8.5f', p)
    stdio.writeln()

#-----------------------------------------------------------------------

# python transition.py < tiny.txt
# 5 5
#  0.02000 0.92000 0.02000 0.02000 0.02000
#  0.02000 0.02000 0.38000 0.38000 0.20000
#  0.02000 0.02000 0.02000 0.92000 0.02000
#  0.92000 0.02000 0.02000 0.02000 0.02000
#  0.47000 0.02000 0.47000 0.02000 0.02000
 
# python transition.py < medium.txt
# (Output omitted.)

