'''
1 for snake 
-1 for water 
0 fro gun 
'''
import random

computer = random.choice([1,0,-1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"s", -1:"w", 0:"g"}
you = youDict[youstr]

print(f"Your choice: {reverseDict[you]}\nComputer Choice: {reverseDict[computer]}")

if(computer == you):
    print("Its draw")

else:
    if(computer == 1 and you == -1):             # c-y = 2
        print("You Lose")
    elif(computer == 1 and you == 0):            # c-y = 1
        print("You Win")
    elif(computer == -1 and you == 0):           # c-y = -1
        print("You Lose")
    elif(computer == -1 and you == 1):           # c-y = -2
        print("You Win")
    elif(computer == 0 and you == 1):            # c-y = -1
        print("You Lose")
    elif(computer == 0 and you == -1):           # c-y = 1
        print("You Win")
    else:
        print("Something went wrong")


'''According to the pattern
if (computer == you):
    print("Its draw")
else:
    if (computer - you == 1 or computer - you == -2):
        print("You Win")
    else:
        print("You Lose")'''