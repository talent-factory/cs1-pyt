# -----------------------------------------------------------------------
# coupon.py
# -----------------------------------------------------------------------

import random
import sys

from stdlib.stdarray import create_1d
from stdlib.stdio import writeln


# -----------------------------------------------------------------------

# Return a random coupon between 0 and n-1.

def get_coupon(number):
    return random.randrange(0, number)


# -----------------------------------------------------------------------

# Collect coupons until getting one of each value in the range
# 0 to n-1.  Return the number of coupons collected.

def collect(number):
    found = create_1d(number, False)
    coupon_count = 0
    distinct_coupon_count = 0
    while distinct_coupon_count < number:
        coupon = get_coupon(number)
        coupon_count += 1
        if not found[coupon]:
            distinct_coupon_count += 1
            found[coupon] = True
    return coupon_count


# -----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of
# each of n types.

n = int(sys.argv[1])
couponCount = collect(n)
writeln(couponCount)

# -----------------------------------------------------------------------

# python coupon.py 1000
# 6456

# python coupon.py 1000
# 8815

# python coupon.py 1000000
# 16079795
