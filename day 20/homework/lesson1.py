# დავალება 1
letters = ["a", "b", "c", "e", "i", "o", "u", "d", "f"]
vowels = ["a", "e", "i", "o", "u"]
vowel_count = sum(1 for letter in letters if letter in vowels)
print(vowel_count)

# დავალება 2
numbers = list(range(1, 51))
multiples_of_5_and_3 = [num for num in numbers if num % 5 == 0 and num % 3 == 0]
print(multiples_of_5_and_3)

# დავალება 3
mixed_list = ["a", "b", "3", "c", "4", "d", "5"]
mixed_string = "".join(mixed_list)
print(mixed_string)

# დავალება 4
for i in range(4):
    print(" " * i + "*" * 6)

# დავალება 5
age = int(input("რამდენი წლის ხარ? "))
if age > 12:
    print("შენ არ ხარ 12 წლის")