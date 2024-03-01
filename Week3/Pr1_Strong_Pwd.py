##split() 
    #is a fonction method used to split a string into a list of substrings based on a specified delimiter.
        ##for example "Mus Ta Pha" into ['Mus','Ta',Pha]
import random
import string
lettres = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
symbols = '!@#$%^&*()":>?<'
Strong_mode_pass =[]
Strong_mode_pass.append(''.join(random.sample(lettres,k=9)))
Strong_mode_pass.append(''.join(random.sample(numbers,k=9)))
Strong_mode_pass.append(''.join(random.sample(symbols,k=9)))
Strong_mode_pass=''.join(Strong_mode_pass)
Strong_mode_pass=random.sample(Strong_mode_pass,k=9)
print(''.join(Strong_mode_pass))



