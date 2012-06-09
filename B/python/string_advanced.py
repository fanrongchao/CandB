# advanced string manipulation 
# most from interviews

import sys
import os
import commands
import re
from sets import Set

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

# reverse polish notation, from my LinkedIn interview
# take a string as input, return computed result as float number
# next: use space to identify numbers...
def reverse_polish(s):
    if len(s) < 1:
        raise ValueError('invalid argument: zero-length string')

    # stack
    stack = list()
    try:
        for ch in s:
            if ch == '+':
                stack.append(stack.pop() + stack.pop()) # may empty list exception
            elif ch == '-':
                t = stack.pop()
                stack.append(stack.pop() - t)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop()) 
            elif ch == '/':
                t = stack.pop()
                stack.append(stack.pop() / t)
            else: # numbers
                stack.append(float(ch)) # may ValueError
        return stack.pop()

    except IndexError as e:
        print 'Input error:', e
    except ZeroDivisionError as e:
        print 'Input error:', e
    except ValueError as e:
        print 'Input error:', e
    except Exception as e:
        print e
        raise


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
      if got == expected:
          print 'OK got: %s' % repr(got)
      else:
          prefix = '  X '
          print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    cases = [
            'abccdwsef',
            'h hh',
            'I love rongchao, hope rongchao love me too @_@'
            ]
    #for c in cases:

    print '**** test binary add by string ****'
    test(bi_add('11111','1'), '100000')
    test(bi_add('1010','1010'), '10100')
    
    print '**** test reverse polish notation (RPN) ****'
    test(reverse_polish('512+3/+9-'), -3.0)
    # exceptions
    reverse_polish('2+40/')
    reverse_polish('21+s0/')
    reverse_polish('21+0/')

if __name__ == '__main__':
    main()
