import random

print('Hello... What is your name?')
name=input()

print('Good to meet you, '+name+'. I am thinking of a number between 1 and 20. Take a guess.')
secretnumber=random.randint(1,20)

for guessestaken in range(1,7):
    print('Take a guess.')
    guess=int(input())

    if guess< secretnumber:
        print('Thats too low.')
    elif guess>secretnumber:
        print('Your guess is too high.')
    else:
        break #this condition is for correct guess
if guess ==secretnumber:
    print('Good job, '+name+'. You guessed the number in '+ str(guessestaken)+' guesses.')
else:
    print('No. The number I was thinking of was '+str(secretnumber))
print('You took '+str(guessestaken)+' guesses.')
