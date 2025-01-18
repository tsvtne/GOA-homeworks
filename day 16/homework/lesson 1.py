my_list = [] 

for i in range(4):
    element = input(f"შეიყვანეთ ელემენტი #{i + 1}: ")
    my_list.append(element)

my_list.append("სტატიკური ელემენტი")

print("\nსიაში არსებული ელემენტები:")
for element in my_list:
    print(element)