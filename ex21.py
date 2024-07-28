'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''
# Write a function called valid_parentheses that takes a string of parentheses,
# and determines if the order of the parentheses is valid. valid_parentheses
# should return true if the string is valid, and false if it's invalid.
def valid_parentheses(string):
    r = 0
    i = 0
    while i < len(string):
        if string[i] == '(':
            r += 1
        if string[i] == ')':
            r -= 1
        if r < 0:
            return False
        i += 1
    return r == 0
