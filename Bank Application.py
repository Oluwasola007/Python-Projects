
print("welcome to Oluwasola's Bank")
restart=('Y')
chance = 3
balance = 1000000.00
while chance >= 0:
    pin = int(input("please enter your pin: "))
    if pin == (1996):
        print("You Entered your pin correctly ")
        while restart not in ('n','NO','no','N'):
            print('press 1 for your Balance\n')
            print('press 2 To Make a Withdraw \n')
            print('press 3 To to pay in \n')
            print('press 4 To Return Card\n')
            option = int(input('What would you like to choose?: '))
            if option == 1:
                print('your Balance is N',balance,'\n')
                restart = input('Would you like to go back? ')
                if restart in ('n','NO','n','N'):
                    print('Thank you')
                    break
            elif option == 2:
                option2 =('y')
                withdraw = float(input("How Much Would you like to withdraw? \n N1000/N2000/N5000/N10000/N20000/N40000: "))
                if withdraw in [1000,2000,5000,10000,20000,40000]:
                    balance = balance - withdraw
                    print('\n Your Balance is Now N',balance)
                    restart = input('Would you like to go back? ')
                    if restart in ('n','N','NO','no'):
                        print("Thank you")
                        break
                elif withdraw != [1000,2000,5000,10000,20000,40000]:
                    print("Invalid Amount, Please re-try\n")
                elif withdraw == 1:
                    withdraw = float(input('Please Enter Desired amount:'))
            elif option == 3:
                pay_in = float(input('How Would You like to Pay In'))
                balance = balance + pay_in
                print("\n Your Balance is Now N",balance)
                restart = input('Would You Like to Go Back? ')
                if restart in ('n', 'N', 'NO', 'no'):
                    print("Thank you for banking with us!")
            elif option == 4:
                print('Please wait whilst your card is being Returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number.\n')
                restart = ('y')
    elif pin !=('1996'):
        print('Incorrect password')
        chances = chance - 1
        if chances == 0:
            print('\n No More Tries')
            break