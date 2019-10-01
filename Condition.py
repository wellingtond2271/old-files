# Conditional 
print("Welcome to Movie Bot ")
age = int(input("How old are you? "))
if age > 17:
	print("You can see R rated movie")
else:
	print("YOU CAN NOT SEE AN R RATED MOVIE YOU FIEND")

print(" Have a great day")

myNum = 4
choice = int(input("Pick a number between 1 and 10:"))
if myNum == choice:
	print("You Guessed it ")
elif choice < myNum:
	print("Too Low")
else:
	print("Too High ")

# == (equal to), <,>,<=,>=,!= (not equal too)

bDay = input("Is today your birthday?yes/no: ")
if bDay== "yes":
	print("Happy Birthday")
elif bDay == "no":
	print("Have a nice day anyway ")
else:
	print(" Learn how to read you baffoon")