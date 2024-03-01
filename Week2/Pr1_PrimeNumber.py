#Writh a fonction that check if a number is a Prime number
def Prime_number(number):
    for i in range(number-2):
        if(number%(i+2)==0):
            return False
    return True
def Test_Exist():
    test_exit=input('C for contnue E for exist : ')
    if test_exit == 'E':
        return True
    else :
        return False
while(True):
    number = int(input('writh a number to check if that number a prime number : '))
    if(Prime_number(number)):
        print(number,'is a prime number')
    else:
        print(number,'is not a prime number')
    if Test_Exist():
        break 
    


