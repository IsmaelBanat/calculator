from math import sqrt, pi
print('SIMPLE CALCULATOR')
while True:
    status = input("Type 'start' or 'end': ")
    if status == "Start" or "start":
        operator = input('Choose operator (+, -, x, /, sqrt): ')
        num_1 = float(input('num_1 is: '))
        num_2 = float(input('num_2 is: '))
        try:
            if operator == '+':
                print(num_1+num_2)
            if operator == '-':
                print(num_1-num_2)
            if operator == 'x':
                print(num_1*num_2)
            if operator == '/':
                print(num_1/num_2)
            if operator == 'sqrt':
                print(sqrt(num_1))
        except:
            print('Invalid operator!')
    elif status == "End" or "end":
        break
    else:
        print("Invalid choice! Choose either 'Start' or 'End'")