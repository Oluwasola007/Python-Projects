import random
min = 1
max = 6 
print("Welcome to dice game developed by Oluwasola")

username = input("Enter your username: ")
print(f"Welcome on board! {username}")
print("Would you like to play this game? (Yes or No): ")

op = input("Enter your option: ")
if op == "yes" and "Yes":
    print("The values are: ")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("would you love to roll again? (Yes or No): ")
    while roll_again == "yes" and "Yes":
        print("The values are: ")
        print(random.randint(min, max))
        print(random.randint(min, max))
        break
    else:
        print(f"Thank you! {username}")

else:
    print(f"Thank you! {username}")