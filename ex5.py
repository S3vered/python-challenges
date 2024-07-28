'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''
# Write a function called vowel_count that accepts a string
# and returns a dictionary with the keys as the vowels and
# values as the count of times that vowel appears in the string.
def vowel_count(accept_string):
    string = accept_string.lower()
    return {char: string.count(char) for char in accept_string if char in "aeiou"}