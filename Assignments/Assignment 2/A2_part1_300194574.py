#Family Name : Scott Makos
#Student number : 300194574
#Class : ITI 1100
#Assigment2 part 1
#Year 2020 

import math
import random

def start():
    '''
    none --> none
    Precondtion: None
    Starts the math quiz / math helper program
    '''
    print("*************************************************")
    print("*        Welcome to my math quiz tool!          *")
    print("*************************************************")
    print(" ")
    name = input("What is your name? ")
    split1 = int(input(f"Hello {name}! Please enter : \n1 if you are in elementary school \n2 if you are in highschool \n3 if none of these apply to you. "))
    if split1 == 1 :
        split2 = input(f"{name} would you like to practise your substraction? Yes or No?" )
        if split2.lower().strip()==  "yes":
            flag = 0
            print("*************************************************")
            print("*              Substraction quiz!               *")
            print("*************************************************")
            n = int(input("How many questions would you like?"))
            print(f"here are your {n} question : ")
            elementary_school_quiz(flag, n)
        elif split2.lower() == "no":
            split3 = input(f"{name} would you like to practise your exponentiation? Yes or No?" )
            if split3.lower().strip() == "yes":
                flag = 1
                print("*************************************************")
                print("*              Exponential quiz!                *")
                print("*************************************************")
                n = int(input("How many questions would you like?"))
                print(f"here are your {n} question : ")
                elementary_school_quiz(flag, n)
               
            elif split3.lower().strip() == "no":
                print(f"No options were chosen. If you wish to try again type 'start()'. Goodbye {name}!")
    if split1 == 2 :
        print("*************************************************")
        print("* Quadratic equation (a*x^2 + b*x + c) solver!  *")
        print("*************************************************")
        split4 = input(f"{name} would you like to solve a quadratic equation? Yes or No?" )
        if split4.lower().strip() == "yes" :
            while split4.lower().strip()== "yes" :
                a =float(input("Please input coefficient a"))
                b =float(input("Please input coefficient b"))
                c =float(input("Please input coefficient c"))
                high_school_quiz(a,b,c)
                print("")
                split4 = input("Would you like to solve another equation? Yes or no? ")
            else :
                print(f"Thank you for using our program {name}. Feel free to use it again.")
              
        elif split4.lower().strip() == "no" :
            print(f"Okay! Thank you for using our program {name}. Feel free to try it again!")
    if split1 == 3 :
        print("This program is to test elementary school kids and help highschool students.\nThis program will most likely not have any use for you. If it does feel \nfree to use this program again by typing start().")
    elif split1 > 3 :
        print("Only values 1 , 2 and 3 are accepted. Please try again")
        print(f"Goodbye {name}")

def elementary_school_quiz(flag, n):
    '''
    (number, number) --> none
    Precondtion: flag == 0 or 1, n > 0, n == type(int)
    program for elementary school math test
    '''
    if flag == 0 :
        correct = 0
        for n in range(n):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            question = n1-n2
            print(f"question {n+1} :")
            ans = int(input(f" What is {n1} - {n2}? "))
            if ans == question :
                print("You are correct.")
                correct = correct +1
            
            else :
                print("That is not correct.")
        ratio =  correct / (n +1)
        print(f"You answered {correct}/{n +1} answers correctly!")
        if 1 > ratio >= 0.50 :
            print(f"Good job, but I know you can do better! Feel free to try again.")
        elif ratio == 1 :
            print(f"Good job, You will probably get an A tommorow! Goodbye.")
        elif ratio >= 0 <= 0.5 :
            print(f"I think you might need a little more practise! Feel free to try again. Bye.")

    if flag == 1 :
        correct = 0
        for n in range(n):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            question = n1**n2
            print(f"question {n+1} :")
            ans = int(input(f"What is {n1}^{n2}? "))
            if ans == question :
                print("You are correct.")
                correct = correct +1
    
            else :
                print("That is not correct")
        ratio =  correct / (n +1)
        print(f"You answered {correct}/{n +1} answers correctly!")
        if 1 > ratio >= 0.50 :
            print(f"Good job, but I know you can do better! Feel free to try again.")
        elif ratio == 1 :
            print(f"Good job, You will probably get an A tommorow! Goodbye")
        elif ratio >= 0 <= 0.5 :
            print(f"I think you might need a little more practise! Feel free to try again. Bye")
    elif flag >2 :
        print("Sorry but you must select either 1 or 2")
        print("Goodbye.")

       
def high_school_quiz(a,b,c):
    '''
    (number,number, number) --> none
    Precondtion: a,b,c == numbers
    program for highscool quadratic formula solver
    '''
    disc = (b**2) - (4*a*c)
    if a != int and disc <0 :
        part1 = -b/(2*a)
        root1 = (f" {part1}" +"+"+"i*" +str(math.sqrt(abs(disc))/(2*a)))
        root2 = (f" {part1}" +"-"+"i*" +str(math.sqrt(abs(disc))/(2*a)))
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"has the following complexe roots : {root1} and {root2}")   
    elif a != 0 and disc > 0:
        root1 = (-b + math.sqrt(disc))/(2*a)
        root2 = (-b - math.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"has the following real roots : {root1} \n and {root2}")
    
    elif a != 0 and disc == 0:
        root1 = (-b + math.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"only has one real root : {root1}")

    elif a == 0 and b== 0 and c == 0 :
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print("is satisfied by all number for x") 

    elif a == 0 and b == 0 :
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(" The equation is satisfied for no number for x")

    elif a == 0 :
        line1 = -c /b
        print(f"the linear function : {b}*x + {c}")
        print(f"has the following root/solution x={line1}")

