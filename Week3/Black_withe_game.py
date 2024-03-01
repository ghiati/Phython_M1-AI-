import random
def ganerate_number():
    numbers='1234567890'
    return random.sample(numbers,k=4)

def check(String_number):
    whithe=0
    black=0
    String_number=list(String_number)
    for i in range (len(String_number)):
        for j in range(4-i,4):
            if ganerate_number()[j]==String_number[i]:
                if i==j:
                    whithe = whithe +1
                else:
                    black=black+1
    print(''.join(ganerate_number()))
    print('you have ',whithe,'white','and ',black,'black\n')
    print('withe mean the number and orrder correct\nblack mean the number correct but the orrder not')
    

def test_Exist():
    test = input ('Writh C for continue Or E for Exist : ')
    if test == 'C' or test =='c':
        return True
while(test_Exist()):
    number =(input('writh a number : '))
    check(number)




