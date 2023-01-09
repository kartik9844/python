# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
 # This condition is the correct guess!
    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

# this the output of program
# I am thinking of a number between 1 and 20.
# Take a guess.
# 5
# Your guess is too low.
# Nope. The number I was thinking of was 17
# Take a guess.
# 11
# Your guess is too low.
# Nope. The number I was thinking of was 17
# Take a guess.
# 18
# Your guess is too high.
# Nope. The number I was thinking of was 17
# Take a guess.
# 19
# Your guess is too high.
# Nope. The number I was thinking of was 17
# Take a guess.
# 8
# Your guess is too low.
# Nope. The number I was thinking of was 17
# Take a guess.