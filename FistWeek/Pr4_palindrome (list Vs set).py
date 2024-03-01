#difference between a list and set :
    ##Ordering:
        #List: Keeps things in order, like a shopping list where items are listed in a particular sequence.
        #Set: Doesn't care about order, it's like a bag where you throw things in, but you don't know in what order they'll come out.
    ##Duplicates :
        #List: Allows repeating the same thing multiple times. It's like having the same item listed multiple times on your shopping list.
        #Set: Each thing is unique, like having a collection of different stamps, you won't have two of the same.
    ##Changing Things:
        #List: You can add, remove, or change items in your list, just like adding or removing items from a shopping list.
        #Set: You can add or remove things, but once they're in, you can't change them individually.

liste1= ['mus','ta','pha']
print(liste1)
ensemble = set(liste1) #breaking a list into a set
print(ensemble)
#Writing a program that checks if a word is a palindrome (for exemple 'abcba' is palindrome)
def Reverse_word(word):
    word1=list(word)
    word2 = word1[::-1] #reverse a list with the operation [::-1]
    return ''.join(word2)
while (True):
    word= input('writh a word to check if that word is palindrome : ')
    if word == Reverse_word(word):
        print(word,' is palindrome')
    else:
        print(word,' is not palindrome')

