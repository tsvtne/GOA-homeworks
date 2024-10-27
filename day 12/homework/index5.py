users = []
while True:
    username = input("შეიყვანეთ მომხმარებლის სახელი (შეწყვიტეთ 'exit'): ")
    if username.lower() == 'exit':
        break
    email = input("შეიყვანეთ ელფოსტა: ")
    password = input("შეიყვანეთ პაროლი: ")
    users.append({'username': username, 'email': email, 'password': password})
    print("მომხმარებელი რეგისტრირებულია!")
print("რეგისტრირებული მომხმარებლები:", users)