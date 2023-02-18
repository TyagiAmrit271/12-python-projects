import random ##for importing random library
def guess(x):
    random_num = random.randint(1,x) ## calling randint function to generate random integer between 1 and X
    guess = 0
    while guess!=random_num:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess < random_num:
            print("Try higher")
        elif guess > random_num:
            print("Try lower")

    print (f"Correct you have guessed{random_num}")
guess(10)
