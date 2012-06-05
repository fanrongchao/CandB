# simple string manipulation 

import sys
import os
import commands
import re
from sets import Set

# reverse a list
def reverse(s):
    if len(s) < 2:
        return s
    i, j = 0, len(s) - 1
    while i < j: # does python have for loop?
        if s[i] != s[j]:
            s[i], s[j] = swap(s[i], s[j])

        i += 1
        j -= 1
    return s

# reverse a string...
def reverse_str(s):
    # reverse a list
    def reverse(s):
        if len(s) < 2:
            return s
        i, j = 0, len(s) - 1
        while i < j: # does python have for loop?
            if s[i] != s[j]:
                s[i], s[j] = swap(s[i], s[j])

            i += 1
            j -= 1
        return s
    
    return ''.join(reverse(list(s)))


def swap(x, y):
    if x != y:
        t = x
        x = y
        y = t
    return (x, y)

# if all chars in the string unique. 
# with extra space True, O(n)
# with extra space False, O(n^2). can be faster???
def is_chars_unique(s, extra): 
    if len(s) < 2:
        return True

    if extra:
        charset = Set()
        for c in s:
            if c in charset:
                return False
            else:
                charset.add(c) 
        return True
    else:
        i = 0
        while i < len(s):
            for c in s[i + 1 : ]:
                if c == s[i]:
                    return False
            i += 1
        return True

# if 2 strings are anagrams or not
# since python's sorted() will not change the string, 
# simple use this method...and compare the returned lists
# O(nlogn)
def is_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    return sorted(s1) == sorted(s2)

# replace all spaces with '%20' - useful in url parse
# python build-in function: string.replace(old, new, [count])
# Note: cannot done in-place since pythong str is immutable
def replace_space(s):
    result = list()
    i = 0
    for c in s:
        if c == ' ':
            result.append('%')
            result.append('2')
            result.append('0')
            i += 3
        else:
            result.append(c)
            i += 1
    return ''.join(result)

# follow-up: replace(old, new)...
# Note: when concat string in python, list's join() is usually fastest
def my_replace(s, old, new):
    indices = set([i.start() for i in re.finditer(old, s)]) # the complexity...
    if len(indices) == 0:
        print 'no old in the string'
        return s # no occurence
    
    result = list()
    i = 0 
    while i < len(s):
        if (i in indices):
            for c in new:
                result.append(c)
                i += 1
        else:
            result.append(s[i])
            i += 1

    return ''.join(result)


# remove duplicate chars in a string without extra space
#def remove_dup(s):


# check if s2 is a rotation of s1 using is_substring
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    def is_substring(s1, s2):
        return s1.find(s2) != -1

    return is_substring(s1 + s1, s2)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
      if got == expected:
          prefix = ' OK '
      else:
          prefix = '  X '

      print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    # test list...
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
            'abcdwsef',
            'h hh',
            'I love rongchao, hope rongchao love me too @_@'
            ]
    for c in cases:
        test(reverse_str(c), c[::-1])
        test(is_chars_unique(c, False), False)
        test(replace_space(c), c.replace(' ', '%20'))
        test(my_replace(c, 'rongchao', 'Danielle'), 
                c.replace('rongchao', 'Danielle'))

    test(is_anagrams('abeed23', 'e2aeb3d'), True)
    test(is_rotation('waterbottle', 'erbottlewat'), True)
    test(is_rotation('ri', 'i'), False)

if __name__ == '__main__':
    main()
