#  https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python 
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l