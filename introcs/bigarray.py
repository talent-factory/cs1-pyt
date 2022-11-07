# -----------------------------------------------------------------------
# bigarray.py
# -----------------------------------------------------------------------

import sys

from stdlib import stdarray
from stdlib import stdio

n = int(sys.argv[1])
a = stdarray.create1d(n, 0)
stdio.writeln('finished')

# -----------------------------------------------------------------------

# python bigarray.py 100000000
# finished

# python bigarray.py 1000000000
# finished

# python bigarray.py 10000000000
# Killed: 9
