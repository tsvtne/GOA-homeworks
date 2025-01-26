# 1) https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
def boolean_to_string(b):
    return str(b)
# 2) https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
# 3)https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
def maps(a):
    return [x * 2 for x in a]
# 4)https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]
# 5) https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python 
def abbrev_name(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"
