# simple string manipulation 
# most from CareerCup Ch1

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


# remove duplicate chars in a string
def remove_dup(s, extra):
    if len(s) < 2:
        return s

    print s
    l = list(s)
    # with extra space (hashSet), O(n)
    if extra:
        charset = Set()
        charset.add(l[0]) 
        remove = 1
        for i in range(1, len(l)): 
            if l[i] not in charset:
                charset.add(l[i])
                l[remove] = l[i]
                remove += 1
        # end iteration, only keep chars before 'remove'
        i = len(l) - 1
        while i >= remove:
            l.pop()
            i -= 1
    # no extra space, O(n^2)
    else:
        remove = 1
        for cur in range(1, len(l)): 
            i = 0
            while i < remove:
            #for i in range(0, remove):
                if l[i] == l[cur]:
                    break
                i += 1
            if i == remove:
                if remove != cur:
                    l[remove] = l[cur]
                remove += 1
            # end iteration, only keep chars before 'remove'
        i = len(l) - 1
        while i >= remove:
            l.pop()
            i -= 1

    return ''.join(l)


# check if s2 is a rotation of s1 using is_substring
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    def is_substring(s1, s2):
        return s1.find(s2) != -1

    return is_substring(s1 + s1, s2)


# binary add function, my facebook interview...
# return a string in binary format
def bi_add(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    len1 = len(s1)
    len2 = len(s2)
    if len1 < 1 or len2 < 1:
        raise ValueError('invalid argument: zero-length string')

    # covert to list, pad to same length
    if len1 > len2:
        s2 = list('0') * (len1 - len2) + s2
    else:
        s1 = list('0') * (len2 - len1) + s1
    r = list()
    carry = 0
    for i in reversed(range(0, len(s1))):
        tmp = (int(s1[i]) + int(s2[i]) + carry)
        if tmp > 1:
            carry = 1
            r.append(0 if tmp == 2 else 1)
        else:
            carry = 0
            r.append(tmp)
    if carry == 1:
        r.append(1)

    return ''.join(map(str,list(reversed(r)))) 


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
      if got == expected:
          print 'OK got: %s' % repr(got)
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
            'abccdwsef',
            'h hh',
            'I love rongchao, hope rongchao love me too @_@'
            ]
    for c in cases:
        print '*****test reverse string'
        test(reverse_str(c), c[::-1])
        print '*****test is char unique'
        test(is_chars_unique(c, False), False)
        print '*****test replace space in string'
        test(replace_space(c), c.replace(' ', '%20'))
        print '*****test replace(old, new)'
        test(my_replace(c, 'rongchao', 'Danielle'), 
                c.replace('rongchao', 'Danielle'))

    print '*****test if 2 strings anagrams'
    test(is_anagrams('abeed23', 'e2aeb3d'), True)
    print '*****test s1 is s2 rotation' 
    test(is_rotation('waterbottle', 'erbottlewat'), True)
    test(is_rotation('ri', 'i'), False)
    print '*****test remove duplicate chars in a string'
    test(remove_dup('abeed223', True), 'abed23')
    test(remove_dup('abeed223', False), 'abed23')
    print '*****test binary add by string'
    test(bi_add('11111','1'), '100000')
    test(bi_add('1010','1010'), '10100')

if __name__ == '__main__':
    main()
