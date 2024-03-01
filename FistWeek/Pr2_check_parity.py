# Write a program that determines if a number is even or odd (pair ou impair)
def check_parity(): 
    number=int(input('Write a number to test if it is even or odd : '))
    if(number%2 == 0):
        print(number,'is even ')
    else:
        print(number,'is odd')
while(True):
    check_parity()
