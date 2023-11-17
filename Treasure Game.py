print("Welcome to Treasure Island")
direction=input("go left or right?")
if direction=="left":
    swimorwait=input("swim or wait?")
    if swimorwait=="wait":
        door=input("which door?")
        if door=="red":
            print("Burned by fire. Game over.")
        elif door=="yellow":
            print("You Win!")
        elif door=="blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over")
        
        
    else:
        print("Attacked by trout. Game over.")


else:
    print("Fall into a hole. Game over")