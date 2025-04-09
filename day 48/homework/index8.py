def is_isogram(string):
    lowercase_string = string.lower()
    unique_letters = set(lowercase_string)
    return len(unique_letters) == len(lowercase_string)