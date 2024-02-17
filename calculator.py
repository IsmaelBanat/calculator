from math import sqrt, pi
print('SIMPLE CALCULATOR')
while True:
    status = input("Type 'start' or 'end': ")
    if status == "Start" or "start":
        operator = input('Choose operator (+, -, x, /, sqrt): ')
        try:
            num_1 = float(input('num_1 is: '))
            num_2 = float(input('num_2 is: '))
        except:
            print('Invalid number!')
        try:
            if operator == '+':
                print("The end result is: ", num_1+num_2)
            if operator == '-':
                print("The end result is: ", num_1-num_2)
            if operator == 'x' or '*':
                print("The end result is: ", num_1*num_2)
            if operator == '/':
                print("The end result is: ", num_1/num_2)
            if operator == 'sqrt':
                print("The end result is: ", sqrt(num_1))
        except:
            print('Invalid operator!')
    elif status == "End" or "end":
        break
    else:
        print("Invalid choice! Choose either 'Start' or 'End'")