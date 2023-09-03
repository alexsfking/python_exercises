'''
Delta Generators In mathematics, the symbols Δ and d are often used to denote
the difference between two values. Similarly, differentiation takes the ratio of
changes (ie. dy/dx) for a linear relationship. This method can be applied
multiple times to create multiple 'levels' of rates of change. (A common example
is x (position) -> v (velocity) -> a (acceleration)).

Today we will be creating a similar concept. Our function delta will take a
sequence of values and a positive integer level, and return a sequence with the
'differences' of the original values. (Differences here means strictly b - a,
eg. [1, 3, 2] => [2, -1]) The argument level is the 'level' of difference, for
example acceleration is the 2nd 'level' of difference from position. The
specific encoding of input and output lists is specified below.

The example below shows three different 'levels' of the same input.

input = [1, 2, 4, 7, 11, 16, 22] list(delta(input, 1)) # [1, 2, 3, 4, 5, 6]
list(delta(input, 2)) # [1, 1, 1, 1, 1] list(delta(input, 3)) # [0, 0, 0, 0] We
do not assume any 'starting value' for the input, so the output for each
subsequent level will be one item shorter than the previous (as shown above). If
an infinite input is provided, then the output must also be infinite.

Input/Output encoding Input and output can be any, possibly infinite, iterable.
Possibilities include finite lists and possibly infinite generator objects, but
any iterable must be accepted as input and is acceptable as output.

Difference implementation delta must work for iterables of any objects/types
that implement __sub__ (eg int, float, set, etc). Additional Requirements/Notes:
delta must work for inputs which are infinite values will always be valid, and
will always produce consistent classes/types of object level will always be
valid, and 1 <= level <= 400
'''

def calculate(values):
    values = iter(values)
    prev_value = next(values)
    for value in values:
        yield value - prev_value
        prev_value = value

def delta(values, n):
    for _ in range(n):
        values = calculate(values)
    return values
