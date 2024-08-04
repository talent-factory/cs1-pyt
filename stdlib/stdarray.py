"""
stdarray.py

The stdarray module defines functions related to creating, reading,
and writing one- and two-dimensional arrays.
"""

from stdlib import stdio


# =======================================================================
# Array creation functions
# =======================================================================

def create_1d(length, value=None):
    """
    Create and return a 1D array containing length elements, each
    initialized to value.
    """
    return [value] * length


# -----------------------------------------------------------------------

def create_2d(row_count, col_count, value=None):
    """
    Create and return a 2D array having rowCount rows and colCount
    columns, with each element initialized to value.
    """
    a = [None] * row_count

    for row in range(row_count):
        a[row] = [value] * col_count

    return a


# =======================================================================
# Array writing functions
# =======================================================================

def write_1d(a):
    """
    Write array a to sys.stdout.  First write its length. bool objects
    are written as 0 and 1, not False and True.
    """
    length = len(a)
    stdio.writeln(length)

    for i in range(length):
        # stdio.writef('%9.5f ', a[i])
        element = a[i]
        if isinstance(element, bool):
            if element:
                stdio.write(1)
            else:
                stdio.write(0)
        else:
            stdio.write(element)
        stdio.write(' ')

    stdio.writeln()


# -----------------------------------------------------------------------

def write_2d(a):
    """
    Write two-dimensional array a to sys.stdout.  First write its
    dimensions. bool objects are written as 0 and 1, not False and True.
    """
    row_count = len(a)
    col_count = len(a[0])
    stdio.writeln(str(row_count) + ' ' + str(col_count))

    for row in range(row_count):
        for col in range(col_count):
            # stdio.writef('%9.5f ', a[row][col])
            element = a[row][col]
            if isinstance(element, bool):
                if element:
                    stdio.write(1)
                else:
                    stdio.write(0)
            else:
                stdio.write(element)
            stdio.write(' ')
        stdio.writeln()


# =======================================================================
# Array reading functions
# =======================================================================

def read_int_1d():
    """
    Read from sys.stdin and return an array of integers. An integer at
    the beginning of sys.stdin defines the array's length.
    """
    count = stdio.read_int()
    a = create_1d(count, None)
    for i in range(count):
        a[i] = stdio.read_int()
    return a


# -----------------------------------------------------------------------

def read_int_2d():
    """
    Read from sys.stdin and return a two-dimensional array of integers.
    Two integers at the beginning of sys.stdin define the array's
    dimensions.
    """
    row_count = stdio.read_int()
    col_count = stdio.read_int()
    a = create_2d(row_count, col_count, 0)

    for row in range(row_count):
        for col in range(col_count):
            a[row][col] = stdio.read_int()

    return a


# -----------------------------------------------------------------------

def read_float_1d():
    """
    Read from sys.stdin and return an array of floats. An integer at the
    beginning of sys.stdin defines the array's length.
    """
    count = stdio.read_int()
    a = create_1d(count, None)

    for i in range(count):
        a[i] = stdio.read_float()

    return a


# -----------------------------------------------------------------------

def read_float_2d():
    """
    Read from sys.stdin and return a two-dimensional array of floats.
    Two integers at the beginning of sys.stdin define the array's
    dimensions.
    """
    row_count = stdio.read_int()
    col_count = stdio.read_int()
    a = create_2d(row_count, col_count, 0.0)

    for row in range(row_count):
        for col in range(col_count):
            a[row][col] = stdio.read_float()

    return a


# -----------------------------------------------------------------------

def read_bool_1d():
    """
    Read from sys.stdin and return an array of booleans. An integer at
    the beginning of sys.stdin defines the array's length.
    """
    count = stdio.read_int()
    a = create_1d(count, None)

    for i in range(count):
        a[i] = stdio.read_bool()

    return a


# -----------------------------------------------------------------------

def read_bool_2d():
    """
    Read from sys.stdin and return a two-dimensional array of booleans.
    Two integers at the beginning of sys.stdin define the array's
    dimensions.
    """
    row_count = stdio.read_int()
    col_count = stdio.read_int()
    a = create_2d(row_count, col_count, False)

    for row in range(row_count):
        for col in range(col_count):
            a[row][col] = stdio.read_bool()

    return a


# =======================================================================

def _main():
    """
    For testing.
    """
    write_2d(read_float_2d())
    write_2d(read_bool_2d())


if __name__ == '__main__':
    _main()
