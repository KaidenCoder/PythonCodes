name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18 and age < 51:
    print("Welcome to club 18-50 holidays, {0}". format(name))
else:
    print("I'm sorry.")    