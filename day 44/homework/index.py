# 1) https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
