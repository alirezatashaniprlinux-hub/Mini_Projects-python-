import random

random_int = random.randint(0,101)
chance = 0

while True:
    input_usr = int(input('enter your number : '))
    if random_int> input_usr:
        print('number is bigger')
        chance+=1
    elif random_int<input_usr:
        print('number is lower')
        chance+=1
    else:
        chance+=1
        print(f'you won number was {random_int} in {chance} time')
        
        break