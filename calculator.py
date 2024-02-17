from math import sqrt, pi
operator = input('choose operator: ')
num_1 = input()
num_2 = input()
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
