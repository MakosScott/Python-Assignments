# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 1
# year 2020

import math
import turtle

########################
# Question 1
########################

def f_to_k(t):
    '''
    (number)-> number
    Precondition : t >= -459.67
    Returns the conversion of a certain degree in Fahrenheit into Kelvins
    '''
    k = ((t - 32) * 5/9) + 273.15
    return k

#######################
# Question 2
#######################

def poem_generator():
    '''
    (string,string)-> none
    Preconditions: name = string, city = string
    Prints a poem which incoperates the name and city given.
    '''
    name= input("what is your name?")
    city = input("what city were you born in?")
    print(f" {city} is where this man belongs")
    print("In the beautiful streets, he paces along")
    print("Until a young man asks for his name")
    print(f"He responds {name}, stressed out and in vain")
    print("The man, confused, grabs his cane")
    print("Go back to your cell, since when did you escape?")

#######################
# Question 3
#######################

def impl2loz(w):
    '''
    number-> (int, float)
    preconditions : w > 0
    returns values of l and o where l is the in of w and 0/16 gives its deimcal value
    '''
    l = int(w)
    o = (w - l)*16
 
    return(l,o)

#######################
# Question 4
#######################

def pale(n):
  '''
  number ->bool
  preconditions : n = four digits (exp : 3454), n>0
  Returns True if the number is a pale number, false if not
  '''
  digit1 = n//1000 %10
  digit2 = n//100 %10
  digit3 = n//10 %10
  digit4 = n%10
  a= not(digit1 == digit2 == 3  or digit2== digit3 ==3 or digit3 == digit4 == 3) and not(digit4 % 4 == 0)
  return(a)

#######################
# Question 5
#######################

def bibformat(author,title,city,publisher,year):
    '''
    (string,string,string,string,string)-> string
    preconditions : author=string, title =string, city =string, publisher =string, year =string
    Returns the proper bliblographic format of the information inputed (string).
    '''
    return(f"{author} ({year}).{title}. {city} : {publisher}.")

#######################
# Question 6
#######################
def  bibformat_display():
    '''
    (string,string,string,string,string) -> string
    preconditions: author =string, title =string, city =string,publisher =string, year = string)
    Returns the information inputted in the proper bibliographic format
    '''
    author = input("What is the name of the author?")
    title = input("What is the title of the book?")
    city = input("In what city was the book published?")
    publisher = input("Who published the book?")
    year = input("What year was the book published?")
    print(bibformat(author,title,city,publisher,year))

#######################
# Question 7
#######################
def compound(x, y, z) :
    '''
    (number,number,number)-> bool
    preconditions : x = int,  y = int, z = int
    returns True if x is the only pair number and if the sum of two adjacent number is > 100
    '''
    a = (x%2 == 0 and y%2 != 0 and z%2 != 0) and (x+y >= 100 or  x+z >= 100 or y+z >= 100)
    return(a)

#######################
# Question 8
#######################
def funct(p):
    '''
    (number)-> none
    preconditions : x = int,  y = int, z = int
    returns True if x is the only pair number and if the sum of two adjacent number is > 100
    '''
    r = math.sqrt(math.log((p-10),5))
    print(f"The solution is {r}")

#######################
# Question 9
#######################
def gol(n):
    '''
    number->number
    preconditions :n >= 1
    Returns the minimum number of times n has to be devided by 2 to become <1
    '''
    return math.ceil(math.log(n,2))

#######################
# Question 10
#######################
def draw_rocket():
    '''
    (None) -> none
    Draws a rocket
    '''
    s=turtle.Screen()
    t=turtle.Turtle()
    #draw cabin of rocket

    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.forward(100)
    t.backward(200)
    t.setheading(90)
    t.forward(400)
    t.penup()
    t.goto(100, -300)
    t.pendown()
    t.forward(400)
    t.circle(150,70)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.setheading(270)
    t.circle(150,-70)

    #Draw windows
    t.penup()
    t.goto(-12, 100)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(-12, 0)
    t.pendown()
    t.circle(40)
    t.penup()

    #Draw astronaut
    t.goto(-3, 51)
    t.pendown()
    t.circle(15)
    t.penup()
    t.goto(-5, 45)
    t.pendown()
    t.circle(4)
    t.penup()
    t.goto(5, 45)
    t.pendown()
    t.circle(4)
    t.penup()
    t.goto(7, 35)
    t.pendown()
    t.setheading(90)
    t.circle(6 ,-180)


    #Draw wings?
    t.penup()
    t.goto(100, -300)
    t.pendown()
    t.setheading(320)
    t.forward(100)
    t.setheading(110)
    t.forward(225)
    t.penup()
    t.goto(-100, -300)
    t.pendown()
    t.setheading(220)
    t.forward(100)
    t.setheading(70)
    t.forward(225)
    #Draw flames
    #first half
    t.penup()
    t.goto(80, -300)
    t.pendown()
    t.setheading(260)
    t.forward(75)
    t.setheading(100)
    t.forward(40)
    t.setheading(260)
    t.forward(75)
    t.setheading(100)
    t.forward(40)
    t.setheading(260)
    t.forward(75)
    t.setheading(100)
    t.forward(40)
    t.setheading(260)
    t.forward(75)
    t.setheading(100)
    t.forward(40)
    
    #second half
    t.setheading(260)
    t.forward(40)
    t.setheading(100)
    t.forward(75)
    t.setheading(260)
    t.forward(40)
    t.setheading(100)
    t.forward(75)
    t.setheading(260)
    t.forward(40)
    t.setheading(100)
    t.forward(75)
    t.setheading(260)
    t.forward(40)
    t.setheading(100)
    t.forward(80)

#######################
# Question 11
#######################

def cad_cashier(price,payment):
    '''
    (number,number)-> number
    preconditions : price<payment, price >0, payment >0
    Gives you back how much the cahsier owes you, rounded to the nearest 5 cents
    '''
    diff = (payment - price)
    a = round(diff*100%10)
    b = int(diff*10)
    c = 5*(3<=a<=7)
    return round(((b/10) + (c/100) + 0.1*(a>=8)),2)


#######################
# Question 12
#######################

def min_CAD_coins(price,payment):
    '''
    (number,number)-> string with 5 numbers inside
    preconditions : price<payment, price >0, payment >0
    Tells you the coins you should recieve as change.
    '''
    z = cad_cashier(price,payment)
    y = z*100
    toonie = y//200
    w = y-(toonie*200)
    dollar = w // 100
    u = w -(dollar*100)
    quarter = u//25
    s = u - (quarter*25)
    dime = s//10
    q = s -(dime*10)
    nickel = q // 5
    final = q - (nickel*5)

    return (f"Your change is {toonie} toonie(s), {dollar} dollar(s), {quarter} quarter(s), {dime} dime(s), {nickel} nickel(s)")
    
    
    


