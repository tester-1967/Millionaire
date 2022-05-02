import random
# colors class
class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# clear console
def clear():
    import os
    clear = lambda: os.system('clear')
    clear()

# start page
def startGame():
    print(bcolors.BLUE + "Welcome to the "+bcolors.PINK+"Millionaire"+bcolors.END+bcolors.BLUE+" game\n\n" + bcolors.END)
    print(bcolors.YELLOW+"©Copyright 2020 Juan & Julian Emran, all rights reserved.\n\n"+bcolors.END)
    print(bcolors.BLUE +"Do you want to start the game?\n\n"+ bcolors.END)
    print(bcolors.GREEN + "\nYes press y" + bcolors.END)
    print(bcolors.RED + "No press n" + bcolors.END)
    answer = input()
    clear()
    if(answer == 'y' or answer == 'Y'):
        return True
    else:
        exit()

# instruction page
def instruction():
    print(bcolors.YELLOW +"+Instructions :\n\n"+bcolors.END)
    print(bcolors.UNDERLINE+"-You have two lifelines you can use them only once"+bcolors.END)
    print("1) 50:50\n2)Call friend\n")
    print(bcolors.UNDERLINE+"-Money System :"+bcolors.END)
    print("10 1,000,000$"+bcolors.YELLOW+"\n9 250,000$"+bcolors.END+"\n8 10,000$\n7 "+bcolors.YELLOW+"5,000$"+bcolors.END+"\n6 2,000$\n5 "+bcolors.YELLOW+"1,000$"+bcolors.END+"\n4 500$\n3 300$\n2 200$\n1 100$\n")
    read = input("Are you ready to start ")
    clear()

# show the question to the user
def askQuestion(questionNum,question , option1 , option2 , option3 , option4):
    print(bcolors.UNDERLINE +questionNum+") "+question+" ?"+bcolors.END)
    print("\n"+option1+"          "+option2)
    print(option3+"          "+option4+"\n\n")

# ask the user if want to use lifelines
def askForHelp(fiftyOption,callOption):
    if(fiftyOption or callOption):
        print(bcolors.BLUE+"Do you want to use any lifelines?\n"+bcolors.END)
        if(fiftyOption == True):
            print(bcolors.GREEN+"- Press number 1 to use 50:50 option"+bcolors.END)
        if(callOption == True):
            print(bcolors.GREEN+"- Press number 2 to call a friend for help"+bcolors.END)
        print(bcolors.RED+"- Press number 3 to exit from lifelines"+bcolors.END)
        option = input()
        if(option == '1' and fiftyOption == True):
            return 1
        if(option == '2' and callOption == True):
            print(bcolors.YELLOW+"Your friend guessed the right answer is : ", random.randint(1,4),""+bcolors.END)
            return 2
    return 0

# 50:50 lifelines function 
def fiftyFunction(right,wrong):
    print(bcolors.YELLOW+"The computer removed two incorrect answers"+bcolors.END)
    print("\n"+right+"          "+wrong)

# check the user answer if correct or not
def checkAnswer(userAnswer,correctAnswer):
    if(userAnswer == correctAnswer):
        print('\x1b[6;30;42m' + 'Correct!' + '\x1b[0m')
        key = input("Press any key to continue")
        clear()
    else:
        print('\x1b[0;30;41m' + 'Incorrect!' + '\x1b[0m')
        key = input("Press any key to exit")
        clear()
        return 1
        
# calculation money and earning for the user
def calculateMoney(money,lose):
    if(lose == True):
        if(money <= 1000):
            print(bcolors.RED+"You lost all your money!"+bcolors.END)
        if(money >= 1000 and money < 10000):
            print(bcolors.YELLOW+"You have won 1000$"+bcolors.END)
        if(money >= 10000 and money < 250000):
            print(bcolors.YELLOW+"You have won 5000$"+bcolors.END)
        if(money >= 250000 and money <= 1000000):
            print(bcolors.YELLOW+"You have won 250000$"+bcolors.END)
        
        exit()
    print(bcolors.GREEN+"You have {0}$ \n".format(money)+bcolors.END)
    if(money == 1000000):
        print(bcolors.GREEN+"Congratulations!!"+bcolors.END+bcolors.PINK+" You have won a "+bcolors.END+bcolors.RED+"million dollars!!"+bcolors.END)
        exit()
    print(bcolors.UNDERLINE+"Do you want to keep playing or to forfeit ?\n"+bcolors.END)
    print(bcolors.GREEN+"-Press y to continue"+bcolors.END)
    print(bcolors.RED+"-Press n to exit"+bcolors.END)
    answer = input()
    if(answer == 'n'):
        exit()
    else:
        clear()

# inputs, questions ,options ,correct answers , prices and flags
questions = ['How many minutes in an hour','Where is the Effiel tower located','What is the first programming language','What year Barcelona and Real Madrid (Clasico) game ended with result 6-2','How old was Steve Jobs when he passed away','What year was the first oscar awards','How far is the moon from the earth in KM','Who was the first woman to fly solo across the Atlantic','What is the largest lake in the world','When was the "Mona Lisa" stolen']
option1 = ['1) 100','1) Berlin','1) C language','1) 2009','1) 55','1) 1829','1) 384,150','1) Geraldine Ferraro','1) Caspian Sea','1) 1911']
option2 = ['2) 50','2) Amsterdam','2) Fortan','2) 2008','2) 56','2) 1928','2) 384,400','2) Martha Stewart',' 2) Lake Superior','2) 1798']
option3 = ['3) 60','3) Tel Aviv','3) Java','3) 2010','3) 57','3) 1828','3) 324,305','3) Amelia Earhart','3) Lake Victoria','3) 1510']
option4 = ['4) 30','4) Paris','4) Assembly','4) 2007','4) 58','4) 1929','4) 387,200','4) Sally Ride','4) Aral Sea','4) 1886']
prices = [100,200,300,500,1000,2000,5000,10000,250000,1000000]
rightAnswer = [3,4,2,1,2,4,2,3,1,1]
fiftyFifty = [option2[0],option1[1],option2[2],option1[3],option2[4],option1[5],option1[6],option3[7],option1[8],option1[9]]
fiftyFiftyWrong = [option3[0],option4[1],option4[2],option3[3],option4[4],option4[5],option2[6],option4[7],option3[8],option4[9]]
fiftyFlag = True
callFlag = True
lose = False
 # -----------------------------------------------------
# starting the game
clear()
start = startGame()
if(start):
    instruction()
    # loof for all question and checks 
    for i in range(10):
        askQuestion(str(i+1),questions[i],option1[i],option2[i],option3[i],option4[i])
        help = askForHelp(fiftyFlag,callFlag)
        if(help == 1):
            fiftyFunction(fiftyFifty[i],fiftyFiftyWrong[i])
            fiftyFlag = False
        if(help == 2):
            callFlag = False
        finalAnswer = int(input(bcolors.PINK+"Enter your final answer -> "+bcolors.END))
        checked = checkAnswer(finalAnswer,rightAnswer[i])
        if(checked == 1):
            lose = True
        calculateMoney(prices[i],lose)
