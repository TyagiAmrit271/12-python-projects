import random #to access random library

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!= 'c':
        if low!=high: #if statement to avoid error caused by randit
            guess = random.randint(low,high) #to generate a random number between lower limit which is 1 and higher limit which is defined by user
        else:
            guess = low
        feedback = input(f'is {guess} high(H),low(L), or Correct(C)??').lower() #.lower to convert feedback in lower case 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Your Number is {guess}')
computer_guess(10)
