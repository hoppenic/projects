

#ask user to enter a number then run fizzbuzz on it


userNum=input("Please enter a number between 50 and 100")


for x in range(1,int(userNum)):
    if x % 15==0:
        print(x, "fizzbuzz")
    elif x % 5 == 0:
        print(x,"fizz")
    else:
        print(x,"buzz")
        