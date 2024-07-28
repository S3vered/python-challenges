'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''
# \Write a function called three_odd_numbers,
# which accepts a list of numbers and returns True  if any three consecutive numbers sum
# to an odd number.
def three_odd_numbers(l):
    for i in range(len(l) - 2):
        result = l[i] + l[i + 1] + l[i + 2]
        if result % 2 != 0:
            return True
    return False