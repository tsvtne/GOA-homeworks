# 1
# def vowel_one(s):
#     vowels = "aeiouAEIOU"

#     return ''.join('1' if char in vowels else '0' for char in s)
# 2
# from fractions import Fraction
# def reduce_fraction(fraction):
#     t = Fraction(*fraction)
#     return (t.numerator, t.denominator)

# 3
# def count_letters_and_digits(s):
#     count = 0
#     for char in s:
#         if char.isalpha() or char.isdigit():
#             count += 1
#     return count
# 4
# def solution(text, ending):
#     return text.endswith(ending)
# 5
# def elimination(arr):
#     seen = set()
#     for num in arr:
#         if num in seen:
#             return num
#         seen.add(num)
#     return None