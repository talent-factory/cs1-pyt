# -----------------------------------------------------------------------
# primesieve.py
# -----------------------------------------------------------------------

import sys

from stdlib import stdarray
from stdlib import stdio

# Accept integer n as a command-line argument. Write to standard
# output the number of primes <= n.

n = int(sys.argv[1])

# Initially assume all integers are prime.
is_prime = stdarray.create1d(n + 1, True)

# Mark non-primes <= n using the Sieve of Eratosthenes.
# https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes
for i in range(2, n):
    if is_prime[i]:
        # Mark multiples of i as nonprime.
        for j in range(2, n // i + 1):
            is_prime[i * j] = False

# Count the primes.
count = 0
for i in range(2, n + 1):
    if is_prime[i]:
        count += 1

stdio.writeln(count)

# -----------------------------------------------------------------------

# python primesieve.py 25  
# 9

# python primesieve.py 100
# 25

# python primesieve.py 10000
# 1229

# python primesieve.py 1000000
# 78498

# python primesieve.py 100000000
# 5761455
