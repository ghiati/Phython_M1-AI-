# Write a program that indicates if number is divisible by another number 

def divisibility():
    number2 = int(input('Write a number: '))
    number1 = int(input('Write another number: '))
    if (number2 % number1 == 0):
        print(number2, 'is divisible by', number1)
    else:
        print(number2, 'is not divisible by', number1)

while(True):
    divisibility()
