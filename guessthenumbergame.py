n=18
count=0
guess=raw_input("Enter a number and I will guess if it is correct")
while(count<=9):
    count=count+1
    
    if int(guess)==n:
        print("Congratulations you guessed the number")
        break;
    elif int(guess)>n:
        print("Guess a number lesser than number you guessed")
        guess=raw_input()
    else:
        print("Guess a number greater than number you guessed")
        guess=raw_input()
if count==10:
    print("Sorry game over try next time")
