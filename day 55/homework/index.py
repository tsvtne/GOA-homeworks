# 1
# def solution(text, ending):
#     return text.endswith(ending)
# 2
# def even_or_odd(s):
#     even_sum = sum(int(digit) for digit in s if int(digit) % 2 == 0)
#     odd_sum = sum(int(digit) for digit in s if int(digit) % 2 != 0)

#     if even_sum > odd_sum:
#         return "Even is greater than Odd"
#     elif odd_sum > even_sum:
#         return "Odd is greater than Even"
#     else:
#         return "Even and Odd are the same"

# 3
# def even_numbers(arr, number):
#     even_nums = [num for num in arr if num % 2 == 0]
#     return even_nums[-number:]

# 4
# def vowel_indices(word):
#     vowels = "aeiouyAEIOUY"
#     return [i+1 for i, char in enumerate(word) if char in vowels]
# 5
# def geometric_sequence_elements(a, r, n):
#     sequence = [a * (r ** i) for i in range(n)]
#     return ', '.join(map(str, sequence))
