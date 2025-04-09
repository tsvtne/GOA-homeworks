def binary_array_to_number(arr):
    binary_string = ''.join(map(str, arr))
    return int(binary_string, 2)