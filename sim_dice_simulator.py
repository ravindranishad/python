import random


while True:
    input('enter to roll dice 🎲')# fake input to simulate
    roll = random.radint(1, 6)
    print('you rolled dice and got🎲: ',roll)
    if roll == 1:
        print('🧑‍⚖️you lose!🧑‍⚖️')
        break
    elif roll == 6:
        print('')