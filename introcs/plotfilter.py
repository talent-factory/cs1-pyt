#-----------------------------------------------------------------------
# plotfilter.py
#-----------------------------------------------------------------------

import stdio
import stddraw

# Read x and y scales from standard input, and configure standard
# draw accordingly. Then read points from standard input until
# end-of-file, and plot them on standard draw.

x0 = stdio.read_float()
y0 = stdio.read_float()
x1 = stdio.read_float()
y1 = stdio.read_float()

stddraw.setXscale(x0, x1)
stddraw.setYscale(y0, y1)

# Read and plot the points.
stddraw.setPenRadius(0.0)
while not stdio.is_empty():
    x = stdio.read_float()
    y = stdio.read_float()
    stddraw.point(x, y)

stddraw.show()

#-----------------------------------------------------------------------

# python plotfilter.py < usa.txt

