'''
remove_every_other([1,2,3,4,5]) # [1,3,5]
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1]
# '''
# Write a function called remove_every_other that accepts a list and returns a new list with every second value removed.
def remove_every_other(l):
    return [value for index, value in enumerate(l) if index % 2 == 0]