
from PIL import Image
from datetime import datetime
from datetime import date
import webbrowser
import math
import random
import calendar
class Player:
    points=0
    name=""
    Plyear=0
    Plmonth=0
    Plday=0
    def __init__(self,name):
        self.LOWER = 1
        self.HIGHER = 10
        self.name=""
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)
    def start(self):
        random_number = self.get_random_number()
        print("---------------Guess the randomly generated number from 1 to 10.You have 5 chances good luck ;-)---------")
        chances = 0
        while True:
            try:
                user_number = int(input("Enter the guessed number: "))
                chances += 1
                if user_number == random_number:
                    Player.points+=1
                    print("Bravo!!! You got the Random number!!!","\nYou got 1 point!!")
                    break
                if chances ==5:
                    print("You loss more then 5 chances...try again")
                    break
            except ValueError:
                print("Incorrect input")
    def Calendary():
        today = date.today().year #int
        month=date.today().month #int
        days=date.today().day
        arr=[]
        while True:        
            try:
                x=int(input("Enter year of your birth: "))
                print("1=January,2=February,3=March,4=April,5=May,6=June,7=July,8=August,9=September,10=October,11=November,12=December")
                y = int(input("Press the number of birth month from the list: "))
                z=int(input("Enter the days of your birthday: "))
                if x<=0 or z<=0:    
                     x=int(input("Year must be a number graiter then 0: "))
                if y<=0 or y>12:
                    y = int(input("Month must be a number graiter then 0: "))
                if x>0 and y>0 and z>0:
                    Player.Plyear=today-x
                    Player.Plmonth=month-y
                    Player.Plday=days-z
                    print("You are :",today-x,"years hold","and",month-y,"month","and",days-z,"days")
                    break
            except ValueError:
                 print("Incorrect input")
    def MatematicGame():
        'print("Factorial?Do you know what and how is working?")'
        print("-----------------------------------------------------------")
        print("-------------------------FIRST QUESTION is:\t3! == ?   -----------------")
        print("-------------------------CORRECT ANSWER IS---------------------------------\nAnswer1. =9\tAnswer2.    =6   \tAnswer.3.=   30")
        print("A little help about factorialconcept,please press 10 for reading about it")
        while True:
            try:
                answer=int(input("Choose your answer: "))
                if answer==1 or answer==3:
                        Player.Print()
                        break
                if answer==2:
                        Player.points+=1
                        print("Bravo you got the correct answer(★‿★)!!!","\nYou got 1 point")
                        return 1
                        break
                if answer!=1 or answer!=2 or answer !=3:
                    print("Your answer must be 1,2,3 or 10 for reading about factorial nothing else")
                if answer==10:
                    webbrowser.open("https://en.wikipedia.org/wiki/Factorial")
            except ValueError as var:
                print("Error input,you have to choose from the menu!")
                
    def MathLibraryQuestions():
        print("WELCOME TO Math Library of Python\nMath in Python is a library that have different function like abs,sqrt..")
        x=int(input("Press a number and be in focus :) : "))
        print("Step 1: x = math.sqrt(abs(x)")
        print("Step 2: x = math.pow(x,3)")
        print("Step 3: What wil be the Output  = ??")
        x=math.sqrt(abs(x))
        x=math.pow(x,3)
        while True:
            try:
                answer=int(input("Output is : "))
                if answer==x:
                    Player.points+=1
                    print("Bravo!!!You got the correct answer(★‿★)!!!\nYou got 1 point")
                    return 1
                    break
                if answer!=x:
                    Player.Print()
                    read_about_Math=int(input("Press 10 for reading about library Math : "))
                    if read_about_Math==10:
                        webbrowser.open("https://www.w3schools.com/python/python_math.asp")
                    break
            except ValueError as var:
                print("Error input...")
                
    def LogicQuestioncomplicate():
        while True:
            try:
                print("---------------------------------THIRD QUESTION-------------------------------")
                print("The day before two days after the day before tomorrow is Saturday. What day is it today?")
                print("1=Thursday     2=Friday      3=Saturday")
                answer= int(input("Press your answer: "))
                if answer==2:
                    Player.points+=1
                    print("The “day before tomorrow” is today; “the day before two days after” is really one day after. So if “one day after today is Saturday,” then it must be Friday.")
                    print("Bravo all 3 answers are correct(★‿★)!!!\nYou got 1 point!!!")
                    break
                elif answer!=2:
                    Player.Print()
                    break
            except ValueError as var:
                print("Error input...")
    def LogicQuestioneasy():
        while True:
            try:
                print("---------------------------------SECOND QUESTION-----------------------------")
                print("Five people were eating apples, A finished before B, but behind C. D finished before E, but behind B. What was the finishing order?")
                print("1=CABDE     2=ACBDE      3=DECAB")
                answer= int(input("Press your answer: "))
                if answer==1:
                    print("Bravo you got the correct answer(★‿★)!!!")
                    Player.LogicQuestioncomplicate()
                    break
                elif answer!=1:
                    Player.Print()
                    break
            except ValueError as var:
                print("Error input...")
    
     
    def LogicQuestion():
        point=0
        while True:
            try:
                print("---------------------------------FIRST QUESTION-----------------------------")
                print("There are two ducks in front of a duck, two ducks behind a duck and a duck in the middle. How many ducks are there?")
                print("1=🦆   2=🦆🦆   3=🦆🦆🦆   4=🦆🦆🦆🦆")
                answer= int(input("Press your answer: "))
                if answer==3:
                    print("Bravo you got the correct answer(★‿★)!!!")
                    Player.LogicQuestioneasy()
                    break
                elif answer!=3:
                    Player.Print()
                    break
            except ValueError as var:
                print("Error input...")

    def Guess_My_Name():
        string="Davide"
        temp=[]
        while True:
            indovina=str(input("Guess a letter of my name: "))
            for i in range(len(string)):
                if string[i]==indovina.upper() or string[i]==indovina.lower():
                    print("Bravo!!!You got a letter of my name(✿◠‿◠)!")
                    for j in range(0,i):
                        if not indovina in temp:
                            temp+=string[i]
                            print("All letters you got are: ")
                            print(temp)
                            break
                else:
                    continue
            if indovina.upper()==string.upper()or indovina.lower()==string.lower():
                print("You win!!!My name is Davide!")
                Player.points+=1
                return indovina
                break
    def IQ_Test():
        while True:
            try:
                choise_from1_to5=int(input("Choise from 1 to 5 or 0 to exit from this game: "))
                filename="matematica.jpg"
                filename2="equation.png"
                filename3="iqtest.jpg"
                filename4="questionsimple.jpg"
                filename5="triangles.jpg"
                img=Image.open(filename)
                img2=Image.open(filename2)
                img3=Image.open(filename3)
                img4=Image.open(filename4)
                img5=Image.open(filename5)
                if choise_from1_to5==1:
                    img.show()
                    answer=str(input("Press your answer: "))
                    if answer=="6":
                        Player.points+=1
                        print("Bravo you got the correct answer(★‿★)!!!\nYou got one point!")
                    else:
                        Player.Print()
                if choise_from1_to5==2:
                    img2.show()
                    answer=str(input("Press your answer: "))
                    if answer=="96":
                        Player.points+=1
                        print("Bravo you got the correct answer(★‿★)!!!\nYou got one point!")
                    else:
                        Player.Print()
                if choise_from1_to5==3:
                    img3.show()
                    answer=str(input("Press your answer: "))
                    if answer=="4"or answer=="D" or answer=="d":
                        Player.points+=1
                        print("Bravo you got the correct answer(★‿★)!!!\nYou got one point!")
                    else:
                        Player.Print()
                if choise_from1_to5==4:
                    img4.show()
                    answer=str(input("Press your answer: "))
                    if answer=="182":
                        Player.points+=1
                        print("Bravo you got the correct answer(★‿★)!!!\nYou got one point!")
                    else:
                        Player.Print()
                if choise_from1_to5==5:
                    img5.show()
                    answer=str(input("Press your answer: "))
                    if answer=="13":
                        Player.points+=1
                        print("Bravo you got the correct answer(★‿★)!!!\nYou got one point!")
                    else:
                        Player.Print()
                if choise_from1_to5==0:
                    break
            except ValueError as var:
                    print("You must to choose from 1 to 5 a intiger number...")
    def Remove():
        while True:
            try:
                print("---------------------------------FIRST QUESTION-----------------------------")
                print("arr = [2, 3,'Pippo', 7, 19,5]\narr.remove('5')\nprint('New List: ', arr)")
                print("Answer1.=New List: [2,3,'Pippo',7,5]\tAnswer2.=Error\tAnswer3.=New List: [2,3,'Pippo',7,19]")
                answer=int(input("Press your answer: "))
                if answer==2:
                    print("Bravo you got the correct answer\nThe number 5 his type in array is int but in the parameter of arr.remove('5') his type is string...")
                    Player.Add_In_Array()
                    break
                if answer!=2:
                    Player.Print()
                    break
            except ValueError as var:
                Player.AnswerIndication()
    def Add_In_Array():
        while True:
            try:
                print("---------------------------------SECOND QUESTION-----------------------------")
                print("lista= list(range(3))\nlista.insert(0, 1994)\nlista.insert(-1,'BOOM')\nprint(lista)")
                print("Answer1.=[0,1,2,3,1994,'BOOM']\tAnswer2.=Error\tAnswer3.=: [1994,0,1,2,'BOOM',3]")
                answer=int(input("Press your answer: "))
                if answer==3:
                    print("Bravo you got the correct answer\n")
                    Player.To_confuse_the_user()
                    break
                if answer!=3:
                    Player.Print()
                    break
            except ValueError as var:
                Player.AnswerIndication()
    def To_confuse_the_user():
        while True:
            try:
                print("---------------------------------THIRD QUESTION-----------------------------")
                print("arr=[1,8,4,2,6]\narr.append(5)\narr.sort()\narr.reverse()\nprint(arr[:2])")
                print("Answer1.=[8,6]\tAnswer2.=[1,2,4,5,6,8]\tAnswer3.=: [6,8]")
                answer=int(input("Press your answer: "))
                if answer==1:
                    print("Bravo all 3 answers arecorrect(★‿★)!!!\nYou got 1 point!!!")
                    Player.points+=1
                    break
                if answer!=1:
                    Player.Print()
                    break
            except ValueError as var:
                Player.AnswerIndication()
    def Print():
        print ("Sorry incorrect answer...try again(✿◡‿◡)")
    def AnswerIndication():
        print ("Your answer must be from 1 to 3...try again")
    
def menu():
    print("--------------------------------DAVIDE MENU--------------------------------")
    print("--------------------------WELCOME TO THE ROOM GAME-------------------------\n0.Exit\n1.Details of the Player\n2.Guess the Number\n3.Matematic Game\n4.MathLibraryQuestions\n5.Logic questions\n6.Guess my name\n7.IQ test\n8.Pyhton library\n9.Player details")
    choise = 10
    while  True:
        try:
            if choise == 1:
                while True:
                    try:  
                        name=str(input("Enter your name: "))
                        Player.name=name
                        if name.isnumeric()==False:
                            break
                    except ValueError as var: 
                        print("Error input...")    
                numberGuessingGame = Player(name)
                Player.Calendary()
                menu()
                break
                print("----------------------------------------------------------------")
            elif choise == 2:
                numberGuessingGame = Player(Player.name)
                numberGuessingGame.start()
                menu()
                break
                print("----------------------------------------------------------------")
            elif choise==3:
                print("Matematic question")
                Player.MatematicGame()
                menu()
                break
            elif choise==4:
                print("Math Library Python Question")
                Player.MathLibraryQuestions()
                menu()
                break
            elif choise==5:
                print("In this part you have 3 logic questions if both are corrects you will win one point,good luck :-)")
                Player.LogicQuestion()
                menu()
                break
            elif choise==6:
                Player.Guess_My_Name()
                menu()
                break
            elif choise==7:
                Player.IQ_Test()
                menu()
                break
            elif choise==8:
                Player.Remove()
                menu()
                break
            elif choise==9:
                    print ("Name of Player is: ",Player.name)
                    print("You are : ",Player.Plyear,"years hold",Player.Plmonth,"month","and",Player.Plday,"days")
                    print("Player.points=",Player.points)
                    if Player.points>=6:
                        filewin="win2.jpg"
                        img=Image.open(filewin)
                        img.show()
            elif choise ==0:
                print("exit")
                break
            choise=int(input("CHOOSE FROM DAVIDE MENU: "))
        except ValueError as var:
                print("You must to press a positive from 0 to 9 number...")
menu()
