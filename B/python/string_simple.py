# simple string manipulation 

import sys
import os
import commands
import re

# reverse a list
def reverse(s):
    if len(s) < 2:
        return s
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            s[i], s[j] = swap(s[i], s[j])

        i += 1
        j -= 1
    return s

# reverse a string...
def reverse_str(s):
    return ''.join(reverse(list(s)))

def swap(x, y):
    if x != y:
        t = x
        x = y
        y = t
    return (x, y)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
      if got == expected:
          prefix = ' OK '
      else:
          prefix = '  X '

      print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    # list...
    cases = [
            [],
            [1, 1, 1],
            [-4,-2, 0, 1, 4, 6, 7],
            ]
    for c in cases:
        tmp = c
        tmp.reverse()
        test(reverse(c), tmp)

    # string...
    cases = [
            '',
            'hhh',
            'I love rongchao!!!@_@'
            ]
    for c in cases:
        test(reverse_str(c), c[::-1])

if __name__ == '__main__':
    main()
