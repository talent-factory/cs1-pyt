# -----------------------------------------------------------------------
# intops.py
# -----------------------------------------------------------------------

import sys

from stdlib import stdio

# Accept int command-line arguments a and b. Use them to illustrate
# integer operators. Write the results to standard output.

a = int(sys.argv[1])
b = int(sys.argv[2])

total = a + b
diff = a - b
prod = a * b

quot = a // b

rem = a % b
exp = a ** b

stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(total))
stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
stdio.writeln(str(a) + ' // ' + str(b) + ' = ' + str(quot))
stdio.writeln(str(a) + ' %  ' + str(b) + ' = ' + str(rem))
stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

# -----------------------------------------------------------------------

# python intops.py 1234 5
# 1234 +  5 = 1239
# 1234 -  5 = 1229
# 1234 *  5 = 6170
# 1234 // 5 = 246
# 1234 %  5 = 4
# 1234 ** 5 = 2861381721051424
