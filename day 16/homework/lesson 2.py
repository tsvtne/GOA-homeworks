numbers = [9, 5, 94, 711, 52, 96, 71, 8]

min_number = float('inf')  # infinity, რომ ყველა სხვა ციფრი ნაკლები იქნება

for num in numbers:
    if num < min_number:
        min_number = num  

print("სიის ყველაზე პატარა ციფრი არის:", min_number)