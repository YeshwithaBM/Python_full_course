import data
import game_art_logo
import random
import os 

def display_accountinfo(account):
    name=account['name']
    decription=account['description']
    country=account['country']
    return f'{name}, {decription}, from {country}'

def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
            
def higherLower(account_2,score):
    continue_flag=True
    while continue_flag:
        account_1=account_2
        account_2=random.choice(data.data)

        while account_1==account_2:
            account_2=random.choice(data.data)

        print(f'Compare 1: {display_accountinfo(account=account_1)}')
        print(game_art_logo.vs)
        print(f'Compare 2: {display_accountinfo(account=account_2)}')

        guess=int(input("Who has more Followers? Type 1 or 2: "))

        follower_count_1=account_1['followers']
        follower_count_2=account_2['followers']

        is_correct=check_answer(guess,follower_count_1,follower_count_2)
        os.system('cls')
        print(game_art_logo.logo)
        if is_correct:
            score+=1
            print(f"You are right. Your score is {score}.")
        else: 
            print(f"You wrong ! .. Your final score is {score}")
            continue_flag=False
        

print(game_art_logo.logo)
score=0
account_2=random.choice(data.data)
higherLower(account_2=account_2,score=score)
