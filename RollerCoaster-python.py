bill=0
height=int(input("what is your height?"))
if height<120:
    print("you cannot play")
else:
    print("You can play")
    age=int(input("How old are you?"))
    if age<12:
        bill=3
        print("need to pay $3")
    elif 18<age<=12:
        bill=5
        print("need to pay $5")
    else:
        bill=8
        print("need to pay $8")
        answer=input("do you need photos? y or n")
        if answer=="y":
            bill+=3
            print(f"you need to pay ${bill}")
        else:
            print(f"you need to pay ${bill}")
        