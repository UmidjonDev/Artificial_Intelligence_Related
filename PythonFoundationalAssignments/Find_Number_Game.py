"""Find Number Game"""

import random as r

def ComputerGamer():
    res=input("Would you like to play anticipatory game(y or n) : ")
    if(res=="y"):
        print("Imagine the number which is higher than 0 and lower than 10(10 is also possible) and I attempt to anticipate : ")
        attempts=0
        start=0
        stop=11
        b=True
        anticipatedDigit=r.sample(range(start, stop), 1)
        while b:
            print(f"Is that {anticipatedDigit[0]} (Write + if the number your imagined number is higher that my prediction and vice versa(-). Write yes if I have found the concealed digit) : ")
            sign=input()
            if(sign=="+"):
                attempts+=1
                start=anticipatedDigit[0]
                anticipatedDigit=r.sample(range(start, stop), 1)
            elif(sign=="-"):
                attempts+=1
                stop=anticipatedDigit[0]
                anticipatedDigit=r.sample(range(start, stop), 1)
            elif(sign=="yes"):
                print(f"The number you imagine is equal to {anticipatedDigit[0]}")
                b=False
            else:
                print("Please follow the instructions")
                b=False
    elif(res=="n"):
        None
    else:
        print("Thank you for such unforgettable experience")
    return attempts

def MyGame():
    attempts=0
    print("I opined one number which is in range of 0-10. Just find it")
    start=0
    stop=11
    b=True
    anticipatedDigit=r.sample(range(start, stop), 1)
    while b:
        number=int(input("MY PREDICTION : "))
        if(number==anticipatedDigit[0]):
            print(f"Yep, you are right. The anticipated number is equal to {number}")
            b=False
        elif(number<anticipatedDigit[0]):
            print("You couldn't find the number and it's higher than your given number")
            attempts+=1
        elif(number>anticipatedDigit[0]):
            print("You couldn't find the number and it's lower than your given number")
            attempts+=1
        else:
            print("Please follow the instructions")
            b=False
    return attempts
ComputerGamer()
MyGame()
if(ComputerGamer()==MyGame()):
    print("It's draw")
elif(ComputerGamer()>MyGame()):
    print("I won")
else:
    print("you won congrats")