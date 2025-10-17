'''
rock = 1
paper = -1
scizzor = 0
'''
import random

def rock_paper_scizzor():
    computer = random.choice([1,-1,0])
    yourstr = input("Enter your choice: ")
    yourDict = {
        "rock" : 1 , 
        "paper" : -1 ,
        "scizzor" : 0
    }
    you = yourDict[yourstr]

    print(f"your choice: {you} \ncomputer's choice: {computer} ")


    if(computer == 0 and you == 1):
        print("You win !!!")
    elif(computer == 0 and you == -1):
        print("You lose !!!")
    elif(computer == 0 and you == 0):
        print("Tie !!!")
    elif(computer == 1 and you == 1):
        print("Tie !!!")
    elif(computer == 1 and you == -1):
        print("You win !!!")
    elif(computer == 1 and you == 0):
        print("You lose !!!")
    elif(computer == -1 and you == 1):
        print("You lose !!!")
    elif(computer == -1 and you == -1):
        print("Tie !!!")
    elif(computer == -1 and you == 0):
        print("You win !!!")

    else:
        print("Something went wrong")
rock_paper_scizzor()
rock_paper_scizzor()
rock_paper_scizzor()
rock_paper_scizzor()