# -----------------------------------------------------------------------
# leapyear.py
# -----------------------------------------------------------------------

from stdlib import stdio
import sys

# Accept an int year as a command-line argument. Write True to
# standard output if year is a leap year.  Otherwise write False.

year = int(sys.argv[1])


is_leap_year = (year % 4 == 0)
is_leap_year = is_leap_year and (year % 100 != 0)
is_leap_year = is_leap_year or (year % 400 == 0)

stdio.writeln(is_leap_year)

# -----------------------------------------------------------------------

# python leapyear.py 2016    
# True

# python leapyear.py 1900 
# False

# python leapyear.py 2000
# True
