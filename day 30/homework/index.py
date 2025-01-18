function positiveSum(arr) {
  let sum = 0;
  
  for(let i = 0; i < arr.length; i++){
    if(arr[i] > 0) {
      sum += arr[i]
    }
  }
  
  return sum;
}
# https://www.codewars.com/kata/5715eaedb436cf5606000381

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
# https://www.codewars.com/kata/515e271a311df0350d00000f

def sum_array(a):
    return sum(a)
# https://www.codewars.com/kata/53dc54212259ed3d4f00071c

function findAverage(array) {
  let sum = 0;
  const length = array.length;
  if(length === 0){
    return 0;
  }
  for(let i = 0; i < length; i++){
    sum += array[i];
  };
  return sum / length;
}
# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return[]
    
    positive_count = sum(1 for num in arr if num > 0)
    negative_sum = sum(num for num in arr if num < 0)
    return[positive_count, negative_sum]
numbers = [4, -1 , 3, -2, -6]
result = count_positives_sum_negatives(numbers)
print(result)
# https://www.codewars.com/kata/576bb71bbbcf0951d5000044