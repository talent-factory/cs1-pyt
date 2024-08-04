# -----------------------------------------------------------------------
# bernoulli.py
# -----------------------------------------------------------------------

import math
import sys

import gaussian
from stdlib import stdarray, stddraw, stdstats, stdrandom

# -----------------------------------------------------------------------

# Accept integers n and trials as command-line arguments.
# Perform trials experiments, each of which counts the number
# of heads found when a fair coin is flipped n times. Then
# draw the results to standard draw. Also draw the predicted Gaussian
# distribution function, thereby allowing easy comparison of the
# experimental results to the theoretically predicted results.

n = int(sys.argv[1])
trials = int(sys.argv[2])

freq = stdarray.create_1d(n + 1, 0)
for t in range(trials):
    heads = stdrandom.binomial(n, 0.5)
    freq[heads] += 1

norm = stdarray.create_1d(n + 1, 0.0)
for i in range(n + 1):
    norm[i] = 1.0 * freq[i] / trials

phi = stdarray.create_1d(n + 1, 0.0)
stddev = math.sqrt(n) / 2.0
for i in range(n + 1):
    phi[i] = gaussian.pdf(i, n / 2.0, stddev)

stddraw.set_canvas_size(1000, 400)
stddraw.set_yscale(0, 1.1 * max(max(norm), max(phi)))
stdstats.plot_bars(norm)
stdstats.plot_lines(phi)
stddraw.show()

# -----------------------------------------------------------------------

# python bernoulli.py 20 100000
