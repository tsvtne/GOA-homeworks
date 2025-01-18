# level 24: 
# ```
# 1) split() ფუნქიცია დაწერეთ split() ფუნქციის გარეშე
def custom_split(string, delimiter):
    result = []
    word = ""
    
    for char in string:
        if char == delimiter:
            if word:  
                result.append(word)
                word = "" 
        else:
            word += char  
            
    if word:  
        result.append(word)
    
    return result

# 2) join() ფუნქიცია დაწერეთ join() ფუნქციის გარეშე
def custom_join(delimiter, string_list):
    result = ""
    
    for i, string in enumerate(string_list):
        if i > 0: 
            result += delimiter
        result += string
        
    return result

# 3) replace() ფუნქიცია დაწერეთ replace() ფუნქციის გარეშე
def custom_replace(string, old, new):
    result = ""
    i = 0
    
    while i < len(string):
        if string[i:i+len(old)] == old:  
            result += new  
            i += len(old)  
        else:
            result += string[i] 
            i += 1
    
    return result

# 4) mini function of calculator 
def mini_calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# 5) input ები გამოყენებით, დავამტოთ იმდენი სიტყვა რმადენიც მომხარებეს სურს და ეს სიტყვეი მოვაქციოთ array ში 
# დავაჯოინოთ და გამოვიტანოთ ტერმინალში 
def join_words():
    words = []
    
    while True:
        word = input("give me a word (or take done): ")
        if word.lower() == 'done': 
            break
        words.append(word)  
    
    result = " ".join(words)  
    print("your words:", result)


join_words()




