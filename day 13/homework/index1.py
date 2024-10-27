# 1. დარიგება 1-დან 50-მდე 2-ის Schrittით
num = 1
while num <= 50:
    print(num)
    num += 2

# 2. კვადრატის დახაზვა "*"
size = 5
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

#   3. მართკუთხედი დახაზვა "*"
width = 7
height = 4
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()

#  4. Nested for loop
for num1 in range(1, 4):
    for num in range(1, 4):
        print(f"num1: {num1}, num: {num}")

#   5. სარეგისტრაციო ფორმა (while loop)
users = []
while True:
    username = input("მომხმარებლის სახელი: ")
    password = input("პაროლი: ")
    email = input("ელ. ფოსტა: ")
    users.append({"username": username, "password": password, "email": email})
    more = input("გსურთ კიდევ დამატება? (y/n): ")
    if more.lower() != 'y':
        break