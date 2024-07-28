'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
# Write a function called same_frequency which accepts two numbers and returns True if
# they contain the same frequency of digits. Otherwise, it returns False.

def same_frequency(num1, num2):
    str_num1, str_num2 = str(num1), str(num2)
    freq1, freq2 = {}, {}
    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1

    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1

    return freq1 == freq2
