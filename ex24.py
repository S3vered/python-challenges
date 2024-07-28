'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# Write a function called mode.
# This function accepts a list of numbers and returns the most frequent number in the list of numbers.
# You can assume that the mode will be unique.
# define mode below:
def mode(l):
    result = 0
    num = l[0]
    for i in l:
        r = l.count(i)
        if r > result:
            result = r
            num = i
    return num

