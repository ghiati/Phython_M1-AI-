#Writh a program for guessing a number between 1 and 100
import random
def check():
    number_guess=random.randint(1,100)
    k=4
    number = int(input('Guess the number chosen by the computer. You have only 5 tries : '))
    for i in range(k):
        if (number_guess == number ):
                k=15
                break
        elif(number_guess < number):
                print('oops the number you chose is to hight chose other one you have only ',k-i-1,'tries : ')
                print(k)
        else:
                print('oops the number you chose is to low chose other oneyou have only ',k-i-1,'tries : ')
        number = int(input('Try again : '))
    return k
if(check()==15):
    print('you win')
else:
    print('oop you lose')
