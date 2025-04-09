# def reverse_words(s):
#     split_word = s.split(" ")[::-1]
#     return " ".join(split_word)


# def count_by(x, n):
#     arr = []
#     for i in range(1, n + 1):
#         arr.append(i * x)
#     return arr


# print(count_by(1, 10))  
# print(count_by(2, 5))  





# def get_planet_name(number):
#     if number == 1:
#         return "Mercury"
#     elif number == 2:
#         return "Venus"
#     elif number == 3:
#         return "Earth"
#     elif number == 4:
#         return "Mars"
#     elif number == 5:
#         return "Jupiter"
#     elif number == 6:
#         return "Saturn"
#     elif number == 7:
#         return "Uranus"
#     elif number == 8:
#         return "Neptune"
#     else:
#         return "Unknown"

# # Example
# print(get_planet_name(3))  # Output: "Earth"
# print(get_planet_name(1))  # Output: "Mercury"
# print(get_planet_name(9))  # Output: "Unknown"






# def human_years_cat_years_dog_years(human_years):
#     if human_years == 1:
#         cat_years = 15
#         dog_years = 15
#     elif human_years == 2:
#         cat_years = 24
#         dog_years = 24
#     else:
#         cat_years = 24 + 4 * (human_years - 2)
#         dog_years = 24 + 5 * (human_years - 2)

#     return [human_years, cat_years, dog_years]

# # Examples
# print(human_years_cat_years_dog_years(1))  # Output: [1, 15, 15]
# print(human_years_cat_years_dog_years(2))  # Output: [2, 24, 24]
# print(human_years_cat_years_dog_years(3))  # Output: [3, 28, 29]
# print(human_years_cat_years_dog_years(5))  # Output: [5, 36, 39]






