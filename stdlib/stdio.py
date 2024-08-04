"""
stdio.py

The stdio module supports reading from standard input and writing to
sys.stdout.

Note:  Usually it's a bad idea to mix these three sets of reading
functions:

-- isEmpty(), readInt(), readFloat(), readBool(), readString()

-- hasNextLine(), readLine()

-- readAll(), readAllInts(), readAllFloats(), readAllBools(),
   readAllStrings(), readAllLines()

Usually it's better to use one set exclusively.
"""

import re
import sys

# -----------------------------------------------------------------------

# Change sys.stdin so it provides universal newline support. 

if sys.hexversion < 0x03000000:
    import os

    sys.stdin = os.fdopen(sys.stdin.fileno(), 'rU', 0)
else:
    sys.stdin = open(sys.stdin.fileno(), 'r', newline=None)


# =======================================================================
# Writing functions
# =======================================================================

def writeln(x=''):
    """
    Write x and an end-of-line mark to standard output.
    """
    if sys.hexversion < 0x03000000:
        # x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.write('\n')
    sys.stdout.flush()


# -----------------------------------------------------------------------

def write(x=''):
    """
    Write x to standard output.
    """
    if sys.hexversion < 0x03000000:
        # x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.flush()


# -----------------------------------------------------------------------

def writef(fmt, *args):
    """
    Write each element of args to standard output.  Use the format
    specified by string fmt.
    """
    x = fmt % args
    if sys.hexversion < 0x03000000:
        # x = unicode(x)
        x = x.encode('utf-8')
    sys.stdout.write(x)
    sys.stdout.flush()


# =======================================================================
# Reading functions
# =======================================================================

_buffer = ''


# -----------------------------------------------------------------------

def _read_reg_exp(reg_exp):
    """
    Discard leading white space characters from standard input. Then read
    from standard input and return a string matching regular expression
    regExp.  Raise an EOFError if no non-whitespace characters remain
    in standard input.  Raise a ValueError if the next characters to
    be read from standard input do not match 'regExp'.
    """
    global _buffer
    if is_empty():
        raise EOFError()
    compiled_reg_exp = re.compile(r'^\s*' + reg_exp)
    match = compiled_reg_exp.search(_buffer)
    if match is None:
        raise ValueError()
    s = match.group()
    _buffer = _buffer[match.end():]
    return s.lstrip()


# -----------------------------------------------------------------------

def is_empty():
    """
    Return True if no non-whitespace characters remain in standard
    input. Otherwise, return False.
    """
    global _buffer
    while _buffer.strip() == '':
        line = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            line = line.decode('utf-8')
        if line == '':
            return True
        _buffer += line
    return False


# -----------------------------------------------------------------------

# noinspection DuplicatedCode
def read_int():
    """
    Discard leading white space characters from standard input. Then
    read from standard input a sequence of characters comprising an
    integer. Convert the sequence of characters to an integer, and
    return the integer.  Raise an EOFError if no non-whitespace
    characters remain in standard input. Raise a ValueError if the
    next characters to be read from standard input cannot comprise
    an integer.
    """
    s = _read_reg_exp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
    radix = 10
    str_length = len(s)
    if (str_length >= 1) and (s[0:1] == '0'):
        radix = 8
    if (str_length >= 2) and (s[0:2] == '-0'):
        radix = 8
    if (str_length >= 2) and (s[0:2] == '0x'):
        radix = 16
    if (str_length >= 2) and (s[0:2] == '0X'):
        radix = 16
    if (str_length >= 3) and (s[0:3] == '-0x'):
        radix = 16
    if (str_length >= 3) and (s[0:3] == '-0X'):
        radix = 16

    return int(s, radix)


# -----------------------------------------------------------------------

def read_all_ints():
    """
    Read all remaining strings from standard input, convert each to
    an int, and return those ints in an array. Raise a ValueError if
    any of the strings cannot be converted to an int.
    """
    strings = read_all_strings()
    ints = []
    for s in strings:
        i = int(s)
        ints.append(i)
    return ints


# -----------------------------------------------------------------------

def read_float():
    """
    Discard leading white space characters from standard input. Then
    read from standard input a sequence of characters comprising a
    float. Convert the sequence of characters to a float, and return the
    float.  Raise an EOFError if no non-whitespace characters remain
    in standard input. Raise a ValueError if the next characters to be
    read from standard input cannot comprise a float.
    """
    s = _read_reg_exp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    return float(s)


# -----------------------------------------------------------------------

def read_all_floats():
    """
    Read all remaining strings from standard input, convert each to
    a float, and return those floats in an array. Raise a ValueError if
    any of the strings cannot be converted to a float.
    """
    strings = read_all_strings()
    floats = []
    for s in strings:
        f = float(s)
        floats.append(f)
    return floats


# -----------------------------------------------------------------------

def read_bool():
    """
    Discard leading white space characters from standard input. Then
    read from standard input a sequence of characters comprising a bool.
    Convert the sequence of characters to a bool, and return the
    bool.  Raise an EOFError if no non-whitespace characters remain
    in standard input. Raise a ValueError if the next characters to be
    read from standard input cannot comprise a bool.

    These character sequences can comprise a bool:
    -- True
    -- False
    -- 1 (means true)
    -- 0 (means false)
    """
    s = _read_reg_exp(r'(True)|(False)|1|0')
    if (s == 'True') or (s == '1'):
        return True
    return False


# -----------------------------------------------------------------------

def read_all_bools():
    """
    Read all remaining strings from standard input, convert each to
    a bool, and return those bools in an array. Raise a ValueError if
    any of the strings cannot be converted to a bool.
    """
    strings = read_all_strings()
    bools = []
    for s in strings:
        b = bool(s)
        bools.append(b)
    return bools


# -----------------------------------------------------------------------

def read_string():
    """
    Discard leading white space characters from standard input. Then
    read from standard input a sequence of characters comprising a
    string, and return the string. Raise an EOFError if no
    non-whitespace characters remain in standard input.
    """
    s = _read_reg_exp(r'\S+')
    return s


# -----------------------------------------------------------------------

def read_all_strings():
    """
    Read all remaining strings from standard input, and return them in
    an array.
    """
    strings = []
    while not is_empty():
        s = read_string()
        strings.append(s)
    return strings


# -----------------------------------------------------------------------

def has_next_line():
    """
    Return True if standard input has a next line. Otherwise return
    False.
    """
    global _buffer
    if _buffer != '':
        return True
    else:
        _buffer = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            _buffer = _buffer.decode('utf-8')
        if _buffer == '':
            return False
        return True


# -----------------------------------------------------------------------

def read_line():
    """
    Read and return as a string the next line of standard input.
    Raise an EOFError is there is no next line.
    """
    global _buffer
    if not has_next_line():
        raise EOFError()
    s = _buffer
    _buffer = ''
    return s.rstrip('\n')


# -----------------------------------------------------------------------

def read_all_lines():
    """
    Read all remaining lines from standard input, and return them as
    strings in an array.
    """
    lines = []
    while has_next_line():
        line = read_line()
        lines.append(line)
    return lines


# -----------------------------------------------------------------------

def read_all():
    """
    Read and return as a string all remaining lines of standard input.
    """
    global _buffer
    s = _buffer
    _buffer = ''
    for line in sys.stdin:
        if sys.hexversion < 0x03000000:
            line = line.decode('utf-8')
        s += line
    return s


# =======================================================================
# For Testing
# =======================================================================

# noinspection PyTypeChecker
def _test_write():
    writeln()
    writeln('string')
    writeln(123456)
    writeln(123.456)
    writeln(True)
    write()
    write('string')
    write(123456)
    write(123.456)
    write(True)
    writeln()
    writef('<%s> <%8d> <%14.8f>\n', 'string', 123456, 123.456)
    writef('formatstring\n')


# -----------------------------------------------------------------------

def _main():
    """
    For testing. The command-line argument should be the name of the
    function that should be called.
    """

    commands = {
        'read_int': read_int, 'read_all_ints': read_all_ints,
        'read_float': read_float, 'read_all_floats': read_all_floats,
        'read_bool': read_bool, 'read_all_bools': read_all_bools,
        'read_string': read_string, 'read_all_strings': read_all_strings,
        'read_line': read_line, 'read_all_lines': read_all_lines,
        'read_all': read_all}

    test_id = sys.argv[1]

    if test_id == 'write':
        _test_write()
    else:
        writeln(commands[test_id]())


if __name__ == '__main__':
    _main()
