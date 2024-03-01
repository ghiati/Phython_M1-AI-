#Writh a programm for the Fibonacci set
def Fibonacci(number):
    if number == 0 or number == 1 :
        return 1
    return Fibonacci(number-1)+Fibonacci(number-2)
def Fib_all_number(number):
    liste1=[]
    for i in range(number+1):
        liste1.append(Fibonacci(i))
    return liste1
def test_Exist():
    test = input ('Writh C for continue Or E for Exist : ')
    if test == 'C' or test =='c':
        return True
while(test_Exist()):
    number = int(input('writh a number : '))
    print(Fib_all_number(number))

    

