from math import *

# coutries = ["Nigeria", "Ghana", "Togo", "Benin"]
# getList = list(coutries)

# def getNameAndAge(name, age):
#     if type(name) == str:
#         print('My name is '+name+ '. and am '+str(age)+' old')
#     else:
#         print('We don\'t know the data type of' + name )

# name = input('Input your name: ').lower()
# age = str(input('Input Your age: ')).lower()


# getNameAndAge(name, age)


# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# op = input('op: ')

# if op == '+':
#     print('The correct answer is', num1+num2)
# elif op == '-':
#     print('The correct answer is', num1-num2)
# elif op == '*':
#     print('The correct answer is:', num1*num2)
# elif op == '/':
#     print('The correct answer is', abs(num1/num2))
# else:
#     print('Invalid operator')

    
names_files = open('C:/Users/HP/Documents/python/name.txt', 'r')
for lines in names_files.readlines():
    print(lines)
names_files.close()


