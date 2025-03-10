'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''
# Write a function called sum_pairs which accepts a list
# and a number and returns the first pair of numbers that sum
# to the number passed to the function.




def sum_pairs(l, num):
    result = set()
    for ls in l:
        res = num - ls
        if res in result:
            return [res, ls]
        result.add(ls)
    return []
