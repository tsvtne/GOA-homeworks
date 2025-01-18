def string_to_array(s):
    return s.split() if s else ['']
# 1)https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

def string_to_number(s):
    return int(s)
# 2)https://www.codewars.com/kata/544675c6f971f7399a000e79

def string_to_number(s):
    return int(s)
# 3)https://www.codewars.com/kata/544675c6f971f7399a000e79

def fake_bin(x):
    return ''.join('0' if int(digit) < 5 else '1' for digit in x)
# 4)https://www.codewars.com/kata/57eae65a4321032ce000002d

def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    highest = max(num_list)
    lowest = min(num_list)
    return f"{highest} {lowest}"
# 5)https://www.codewars.com/kata/554b4ac871d6813a03000035