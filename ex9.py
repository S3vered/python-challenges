'''
repeat('*', 3) # '***'
repeat('abc', 2) # 'abcabc'
repeat('abc', 0) # ''
'''
# Write a function called repeat, which accepts a string and a number
# and returns a new string with the string passed to the function repeated the number amount of times. Do not use the built in repeat method!
def repeat(string, n):
    if n == 0:
        return ""
    i = 0
    st = ""
    while i < n:
        st += string
        i += 1
    return st
