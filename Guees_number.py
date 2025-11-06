import random
import csv
users = []


def commit():
    with open('data.csv' , 'w' ,newline='') as f:
        writer = csv.writer(f)
        writer.writerows(users)
def add_user(username):
    users.append([username,0])
    commit()
def check_user(username):
    for i in users:
        if i[0] == username:
            return False
    return True
def sign_up(username):

    if check_user(username):
       

        add_user(username)
        

def read_users():
    with open('data.csv' , 'r' , newline='')as f :
        reader = csv.reader(f)
        return list(reader)
    
def give_score(username):
    for i in users:
        if i[0] == username :
            return i[1]
def update(username,score):
    for i in users:
        if i[0] == username:
            i[1] = score
            commit()
        
def game(username):
    random_int = random.randint(0,101)
    chance = 0
    score =0
    if not check_user(username):
        score=int( give_score(username))
    

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
            newscore = round((10/chance)*100)
            print(f'you won number was {random_int} in {newscore} score')
            
            if score>newscore:
                update(username , score)
            else:
                update(username , newscore)
            break
        
def bestplayer():
    global users
    max = 0
    player = ''
    for i in users:
        if int(i[1])>max:
            max = int(i[1])
            player = i[0]
    print(f'{player} with {max} is best player')

def main():
    global users
    users = read_users()
    username = input('enter your name (username for game) : ')
    sign_up(username)
    bestplayer()
    game(username)
    


if __name__ == "__main__":
    main()