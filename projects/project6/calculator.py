import os
def calculate(first_element):
    while True:
        choose_operation=input("pick an operation: ")
        next_number=float(input("enter next number: "))
        if choose_operation=='+':
            result=first_element+next_number
            print(f'{first_element}+{next_number}={result}')
        elif choose_operation=='-':
            result=first_element-next_number
            print(f'{first_element}-{next_number}={result}')
        elif choose_operation=='*':
            result=first_element*next_number
            print(f'{first_element}*{next_number}={result}')
        elif choose_operation=='/':
            if next_number==0:
                print("Can't divide by 0")
                continue
            else:
                result=first_element/next_number
                print(f'{first_element}/{next_number}={result}')
        else:
            print("invalid option")
            return 

        ask_again=input(f"enter 'y' to continue with {result} or 'n' to start new calculation or 'x' to exit: ").lower()
        if ask_again=='y':
            return calculate(result)
        elif ask_again=='n':
            os.system('cls')
            new_element=float(input("enter a number: "))
            operator=["+","-","/","*"]
            for i in operator:
                print(i)
            return calculate(new_element)
        else:
            break
first_element=float(input("enter a number: "))
operator=["+","-","/","*"]
for i in operator:
    print(i)

calculate(first_element)