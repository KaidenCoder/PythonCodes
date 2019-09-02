parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9] 

numbers = even + odd
numbers_in_order = sorted(numbers)

print(numbers_in_order)

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")



 # add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)

