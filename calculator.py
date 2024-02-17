from math import sqrt

print('SIMPLE CALCULATOR')

while True:
    ans = 0
    input_status = input("Type 'start' or 'end': ")
    
    if input_status.lower() == "start":
        operator = input('Choose operator (+, -, x, /, sqrt): ')
        
        try:
            num_1 = float(input('The first number is: '))
            num_2 = float(input('The second number is: '))
        except ValueError:
            print('Invalid number!')
            continue
        
        try:
            if operator == '+':
                ans = num_1 + num_2
                print("Your answer is: ", ans)
            elif operator == '-':
                ans = num_1 - num_2
                print("Your answer is: ", ans)
            elif operator == 'x' or operator == '*':
                ans = num_1 * num_2
                print("Your answer is: ", ans)
            elif operator == '/':
                ans = num_1 / num_2
                print("Your answer is: ", ans)
            elif operator == 'sqrt':
                ans = sqrt(num_1)
                print("Your answer is: ", ans)
            else:
                print('Invalid operator!')
                continue
        
        except ZeroDivisionError:
            print("Error: Division by zero!")

    elif input_status.lower() == "end":
        break

    else:
        print("Invalid choice! Choose either 'Start' or 'End'")

