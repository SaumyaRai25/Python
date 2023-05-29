import random
l=["rock","scissor","paper"]
while True:
    Ccount=0
    ucount=0
    uc = int(input('''
    Game start....
    1 yes
    2 NO|exit
    '''))
    if uc ==1:
        for a in range (1,6):
            userInput=int(input('''
            1.Rock
            2.Scissor
            3.paper
             '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("user Value",uchoice)
                print("Game Draw")
                ucount = ucount+1
                Ccount = Ccount+1
            elif(uchoice=="rock"and Cchoice=="Scissor")or(uchoice=="paper"and Cchoice=="rock")or(uchoice=="scissor"and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("user value",uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("user Value",uchoice)
                print("computer win")
                Ccount = Ccount +1
    else:
        break            

      