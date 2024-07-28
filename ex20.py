'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''
# Write a function called is_odd_string which returns true if sum of each character's position
# in the alphabet is odd. For example, "a" is in the first position,
# "b" is in the second position, and so on. If the sum is even, return false.
# NOTE: INDEXING STARTS AT 1.  A is position 1, NOT POSITION 0.

def is_odd_string(l):
    result = sum((ord(r) - 96) for r in l.lower()) or 0
    return result % 2 == 1


