# binary search a sorted array

import sys
import os
import commands
import re

# binary search a sorted array
# assuming unique elements
# return the index of the key, -1 if not found
def binary_search(arr, key, low, high):
    print 
    if len(arr) < 1:
        print 'empty array'
        return -1

    print str(arr) +': searching ' + str(key)
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
  
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
      if got == expected:
          prefix = ' OK '
      else:
          prefix = '  X '

      print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    cases = [
            [],
            [-4,-2, 0, 1, 4, 6, 7]
            ]
    test(binary_search(cases[0], 0, 0, len(cases[0]) - 1), -1)
    test(binary_search(cases[1], 0, 0, len(cases[1]) - 1), 2)
    test(binary_search(cases[1], -4, 0, len(cases[1]) - 1), 0)
    test(binary_search(cases[1], 7, 0, len(cases[1]) - 1), 6)
    test(binary_search(cases[1], 2, 0, len(cases[1]) - 1), -1)
    a = ['a','b','e','f']
    test(binary_search(a, 'c', 0, len(a) - 1), -1)


if __name__ == '__main__':
    main()
