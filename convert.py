# PURPOSE: To convert from numbers to strings and vice-versa,
# whilst changing their base representation. Wrapped int() around
# with s2n() for clarity in naming.
# AUTHOR: Andre 'Green

import math

# Not the fastest way to do this but seems to work fine for now
def n2s(n,b):
    num_digits_needed = 1+math.ceil(math.log(n,b))
    s = ""
    while num_digits_needed > 0:
        num_digits_needed -= 1
        d = math.floor(n/(b**num_digits_needed))
        n -= d*(b**num_digits_needed)
        s += str(d)
        if d >= b:
            print("Rounding error: Digit > Base")
    return s

def s2n(n,b):
    return int(n,b)