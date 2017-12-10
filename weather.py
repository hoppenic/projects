
#ask user the temperature
#if <freezing temp print one thing, else print other


userInput=input("What temperature is it?")


if int(userInput)<=32:
	print("The roads could be icy!")
else:
	print("It's not freezing yet!")

