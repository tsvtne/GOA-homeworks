# 1
# def multi_table(number):
#     table = []
#     for i in range(1, 11):
#         product = i * number
#         table.append(f"{i} * {number} = {product}")
#     return '\n'.join(table)

# 2
# def print_array(arr):
#     return ",".join(map(str, arr))

# 3
# def string_clean(s):
#     return ''.join([char for char in s if not char.isdigit()])

# 4
# def remove_consecutive_duplicates(s: str) -> str:
#     if not s:
#         return s
#     words = s.split()
#     result = [words[0]]
#     for word in words[1:]:
#         if word != result[-1]:
#             result.append(word)
#     return ' '.join(result)

# 5
# def between_extremes(numbers):
#     return max(numbers) - min(numbers)