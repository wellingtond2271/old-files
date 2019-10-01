import random

mysteryNum = random.randint(1, 100)
score = 0

while True: 
	guess = int(input("Guess a # from 1 to 100 "))
	score += 1
	if guess == mysteryNum:
		print("Congrats You Guessed it")
		break
	elif guess > mysteryNum:
		print("Too high, Try again ")
	else:
		print("Mwahaha you fool, too low try again")
print("You tried " + str(score) + " times ")