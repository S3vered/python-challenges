'''
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''
# Write a function called find_greater_numbers which accepts
# a list and returns the number of times a number is followed
# by a larger number across the entire list.

def find_greater_numbers(r):
    result = 0
    a = 0
    b = 1
    while a < len(r):
        while b < len(r):
            if r[b] > r[a]:
                result += 1
            b += 1
        b = a + 1
        a += 1
    return result
