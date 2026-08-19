import random
def guessNumber():
    print("let me think of a number between 1 to 60.")
    level_of_difficulty=input("choose the level of difficulty....Type 'easy' or 'hard': ").lower()
    number=random.randint(1,60)
    if level_of_difficulty=='easy':
        attempts=10
    elif level_of_difficulty=='hard':
        attempts=5
    while attempts>0:
        print(f"You have {attempts} remaining to guess the number")
        guess=int(input("Make a guess: "))
        if number==guess:
            print(f"Your guess is right... The answer is {number}")
            return
        elif number<guess:
            print("Your guess is Too High")
        else:
            print("Your guess is Too low")

        attempts-=1

        if attempts>0:
            print("guess again ")
        
    print("Your out of guesses...You lose!!")
    return
guessNumber()
                






            
