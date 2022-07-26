print("Simple Arithmetic Calculator Developed by Oluwasola")
number_1 = int(input("Enter the first number: "))
op = input("Enter operator: ")
number_2 = int(input("Enter the second number: "))

if op == "+":
    answer = number_1 + number_2
    print("The answer is: " + str(answer))

elif op == "-":
    answer = number_1 - number_2
    print("The answer is: " + str(answer))

elif op == "**":
    answer = number_1 ** number_2
    print("The answer is: " + str(answer))

elif op == "/":
    answer = number_1 // number_2
    print("The answer is: " + str(answer))

elif op == "*":
    answer = number_1 * number_2
    print("The answer is: " + str(answer))

elif op == "%":
    answer = number_1 % number_2
    print("The answer is: " + str(answer))

elif op == "//":
    answer = number_1 // number_2
    print("The answer is: " + str(answer))

else:
    print("invalid operator")