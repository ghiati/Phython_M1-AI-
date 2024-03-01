#Rock-Paper-Scissors game between you and computer
import random
liste1 = ['R','S','P']
cumputer_turn=random.choice(liste1)
while(True):
    player=input('chose R for Rock , P for Paper and S for Scissors ')
    if(cumputer_turn==player):
        print('eguality')
        print('the ccumputer chose ',cumputer_turn)
    if ((cumputer_turn == 'R' and player == 's')or (cumputer_turn == 'S' and player == 'P') or (cumputer_turn == 'P' and player == 'R') ):
        print('you lose cumpter win')
        print('the ccumputer chose ',cumputer_turn)
    else:
        print('you win')
        print('the ccumputer chose ',cumputer_turn)
       






