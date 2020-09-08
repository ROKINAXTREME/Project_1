#this is a guess the number game
import random
import time
trys = 0
print ("hi, what's your name?")
name = input()
number = random.randint(1, 100)
print ("So, "+ name+" I am a guess the number game, sub to my youtube at ROKINAXTREME!")
print ("I am thinking of a number 1 - 100 try and guess it in 30 trys.")
for trys in range (30):
    print ('take a guess!')
    guess = input()
    guess = int(guess)
    if guess < number:
        print ("to low!")

    if guess > number:
        print ("To high! Slow down!")
    if guess == number:
        break
if guess == number:
    print ("You guessed it in "+str(trys)+" guesses")
    time.sleep(2)
    if guess != number:
        number = str(number)
        print ("Nope, the number was, "+number+" try again?")
        time.sleep(2)


        
            
    
