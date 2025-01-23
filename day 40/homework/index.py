# 1) https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
def remove_duplicate_words(s):
    result = []
    words = s.split(" ")
    for i in words:
        if i not in result:
            result.append(i)
    return " ".join(result)
    
# 2) https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

# 3) https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python
def solution(nums):
    if not nums:
        return []
    else:
        return sorted(nums)

# 4) https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
def capitals(word):
    capital = []
    for index, i in enumerate(word): 
        if i.isupper():
            capital.append(index) 
    return capital



# 5) https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
