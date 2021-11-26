import random
print ("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")
while chances<5 :
    guess = int(input("Enter your guess :- "))
    if guess == number:
        print("You won!!")
        break
    elif guess < number :
        print("Guess is too low", guess)
    else :
        print("Guess is too high", guess)
    chances += 1
if not chances < 5 :
    print ("You loose! the number is :", number)

