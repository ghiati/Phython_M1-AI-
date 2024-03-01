#writh a programm that gess a word 
import random
ai_words = ["NeuralNetwork", "MachineLearning", "DeepLearning", "Algorithm", "Data", "Model", "Prediction"]
random_word = random.choice(ai_words)
print("Randomly chosen word:", random_word)
def check(lettre):
    whithe=0
    black=0
    for i in range (len(random_word)):
        if random_word[i]==lettre:
            print(lettre)
        else:
            print('_')
                
    print(''.join(random_word))
    print('you have ',whithe,'white','and ',black,'black\n')
    print('withe mean the number and orrder correct\nblack mean the number correct but the orrder not')

print(check('a'))
