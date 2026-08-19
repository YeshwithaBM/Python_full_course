import random

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return 
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is Too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is Too High")
        return attempts-1
    else:
        print(f"Your guess is right... The answer is {answer}")
def game():
    print("let me think of a number between 1 to 60.")
    answer=random.randint(1,50)
    level=input("choose the level of difficulty....Type 'easy' or 'hard': ").lower()
    attempts=set_difficulty(level_chosen=level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("Ypu have entered wrong difficulty level...Play again")
        game()
    guessed_number=0
    while guessed_number!=answer :
        print(f"You have {attempts} remaining to guess the number .")
        guessed_number=int(input("guess a Number: "))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("Your out of guesses...You lose!!")
            return
        elif guessed_number!=answer:
            print("guess again")
game()

    

