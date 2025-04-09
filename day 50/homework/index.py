# 1
# def binary_array_to_number(arr):
#     binary_string = ''.join(map(str, arr))
#     return int(binary_string, 2)

# 2
# def lovefunc(flower1, flower2):
#     return (flower1 % 2) != (flower2 % 2)

# 3
# def lovefunc(flower1, flower2):
#     return (flower1 + flower2) % 2 != 0

# 4
# def is_triangle(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     return a + b > c and a + c > b and b + c > a


# 5
# def longest(a1, a2):
#     combined = a1 + a2
#     unique_chars = sorted(set(combined))
#     return ''.join(unique_chars)

# 6
# def invert(lst):
#     return [ -x for x in lst ]

# 7
# def open_or_senior(data):
#     return ["Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data]

# 8
# def grow(arr):
#     product = 1
#     for num in arr:
#         product *= num
#     return product

# 9
# def printer_error(s):
#     errors = 0
#     for char in s:
#         if char > 'm':
#             errors += 1
#     return f"{errors}/{len(s)}"

# 10
# def dna_to_rna(dna):
#     return dna.replace('T', 'U')