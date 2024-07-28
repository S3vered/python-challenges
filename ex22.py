'''
reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''
# Write a function called reverse_vowels.
# This function should reverse the vowels in a string.
# Any characters which are not vowels should remain in their original position.
# You should not consider "y" to be a vowel.

def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] in vowels:
            j -= 1
        else:
            i += 1
    return "".join(s)
