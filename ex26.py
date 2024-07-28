'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1
'''


# Write a function called letter_counter which accepts a string and returns a function.
# When the inner function is invoked it should accept a parameter which is a letter,
# and the inner function should return the number of times that letter appears.
# This inner function should be case insensitive.


def letter_counter(letter):
    letter_counter.val = letter

    def inner(l):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == l))

    return inner