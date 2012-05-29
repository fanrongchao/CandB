import sys
import os
import commands
import re

# merge two arrays
def merge(a, b):
    result  = []
    len1 = len(a)
    len2 = len(b)
    i, j = 0, 0
    while (i < len1 and j < len2):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    if i == len1 and j == len2:
        return result
    elif i == len1:  #len2 left
        result += b[j:]
        return result
    else:
        result += a[i:]
        return result

# merge sort recursive
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) / 2
    left = merge_sort(arr[: mid])
    right = merge_sort(arr[mid : ])
    return merge(left, right)
  
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
            [3, 4, 0, -3, 4, 2],
            [],
            [0,0,0],
            ['a','bc', 'ax','bb']
            ]

    for arr in cases:
        print arr
        test(merge_sort(arr), sorted(arr))


if __name__ == '__main__':
    main()
