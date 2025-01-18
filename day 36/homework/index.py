# <!-- 1) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python -->
#  def filter_list(l):
#     result = []
#     for item in l:
#         if isinstance(item,int):
#             result.append(item)
#     return result

# 2) https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
# function squareDigits(num){
#   return parseInt(num.toString().split('').map(digit => {
#         const squared = Math.pow(parseInt(digit), 2);
#         return squared.toString();
#     }).join(''));
# }

# 3) https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
# def get_middle(s):
#     length = len(s)
#     mid = length // 2  
#     if length % 2 == 0:
#         return s[mid - 1:mid + 1]
#     else:
#         return s[mid]

# 4) https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
# def find_short(s):
#     return min(len(word) for word in s.split())

# 5) https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
# def solution(text, ending):
#     return text.endswith(ending)