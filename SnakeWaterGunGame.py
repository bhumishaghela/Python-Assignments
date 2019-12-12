import random
def snakeWaterGunGame():
    swg=["Snake","Water","Gun"]
    count=0
    compScore=0
    userScore=0
    while count<11:
        count=count+1
        compChoice=random.choice(swg)
        userChoice=raw_input("Snake Gun or Water?")
        if (compChoice.lower()=="snake" and userChoice.lower()=="water") or (compChoice.lower()=="water" and userChoice.lower()=="gun") or (compChoice.lower()=="gun" and userChoice.lower()=="snake"):
            print("Computer chose "+compChoice)
            print("Computer won a point")
            print("\n")
            print("\n")
            print("\n")
            compScore=compScore+1
            
        elif (userChoice.lower()=="snake" and compChoice.lower()=="water") or (userChoice.lower()=="water" and compChoice.lower()=="gun") or (userChoice.lower()=="gun" and compChoice.lower()=="snake"):
            print("Computer chose "+compChoice)
            print("You won a point")
            userScore=userScore+1
            print("\n")
            print("\n")
            print("\n")
        else:
            print("It's a tie")
        
    if userScore>compScore:
        print("Congratulations you won the game")
    else:
        print("Try next Time Computer won the game")

print("Hello Welcome to Snake Water Gun Game")
print(r""" [][][][][]        ~~~~~~   [][][][]
         [][][:]~  ~~~~~~   []>
                            []""")
while(1):
    snakeWaterGunGame()
    choice=raw_input("Do you want play again y/n?")
    if 'n' in choice:
        break;
                                       

    
    

