# -----------------------------------------------------------------------
# flip.py
# -----------------------------------------------------------------------

import random

from stdlib import stdio

# Simulate a coin flip by writing 'Heads' or 'Tails' to standard
# output.

if random.randrange(0, 2) == 0:
    stdio.writeln('Heads')
else:
    stdio.writeln('Tails')

# -----------------------------------------------------------------------

# python flip.py
# Heads

# python flip.py
# Tails

# python flip.py
# Heads

# python flip.py
# Heads

# python flip.py
# Heads
