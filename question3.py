import random
# Gets a random number between the given range
randomNumber = random.randrange(0, 9)
# Initializing it with a random number coz we just cant declare variables in python
gussedNumber = 99

while gussedNumber != randomNumber:
    
    gussedNumber = int(input("Please write the gussed number: "))
    if gussedNumber == randomNumber:
        print("Congrats dude, You did it. I'm happy for you :)")
        break
    else:
        continue
