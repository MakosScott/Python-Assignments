
import math


#################
#Question 2.1
#################

def sum_odd_divisors(n):
    '''
    (int) --> None or int
    Preconditions: None
    Function that takes n and returns the sum of all its positive odd divisors
    '''
    accum = 0
    if n == 0:
        return None
    else:
        for x in range(1,(abs(n)+1),2):
            if abs(n)%x == 0:
                accum = accum + x
        print(accum)


#################
#Question 2.2
#################

def series_sum():
    '''
    (None) --> number
    Precondtion: n can't be negative
    Functions that returns the sum of the following series 1000 + 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
    '''
    num = int(input("Please enter a positive integer"))
    if num < 0 :
        return None
    else :
        accum = 0
        for i in range(1,(num+1)) :
            accum += ((1)/(i**2))
        return 1000 + accum


#################
#Question 2.3
#################

def pell(n):
    '''
    (int) ---> int
    Preconditions: n >= 0
    Returns the nth pell number
    '''
    num1 = 1
    num2 = 0
    
    if n < 0:
        return None
    elif n == 1:
        ans = 1
    elif n == 0:
        ans = 0
    else:
        for x in range(n-1):
            ans = 2*num1  + num2
            num2 = num1
            num1 = ans

    return ans


################
#Question 2.4
#################

def countMembers(s):
    '''
    (str) ---> int
    Preconditions: Must input a string
    Function that returns the number of characters in s that are extroadinary
    '''
    accum = 0
    for x in s :
        if x in '23456efghijkFGHIJKLMNOPQRSTUVWX,\!' :
            accum += 1
    return accum


#################
#Question 2.5
#################

def casual_number(s):
    '''
    (str) --> int
    Preconditions: Must input a string
    Function that takes the string s and returns an int representing the numbers in that string
    '''
    string = ""
    if "-" in s :
       neg = -1
    else :
        neg = 1
    
    if s.count('-')> 1 :
        return None
    
    for x in s :
         if x in "abcdefghijklmnopqrstuvwxyzx" :
            return None 
         elif x =="," :
            string= string+x.replace(",","")
         elif x in "1234567890" :
            string = string+x
    
    if string == "" :
        return None
    else :
        return (neg *int(string))

#################
#Question 2.6
#################

def alienNumbers(s):
    '''
    (str) ---> int
    Precondition: You must insert a string with the alien symbols
    Function that turns the "alien" symbols in a string and converts them into an integer after summing them up
    '''
    a = s.count("T")
    b = s.count("y")
    c = s.count("!")
    d = s.count("a")
    e = s.count("N")
    f = s.count("U")
    ans = (a*1024)+(b*598)+(c*121)+(d*42)+(e*6)+(f*1)
    return ans
    
#################
#Question 2.7
#################

def alienNumbersAgain(s):
    '''
    (str) ---> int
    Precondition: You must insert a string with the alien symbols
    Function that turns the "alien" symbols in a string and converts them into an integer after summing them up
    '''
    ans = 0
    for c in s :
        if c in "T":
            ans += 1 * 1024
        elif c in "y":
            ans += 1 * 598
        elif c in "!":
            ans += 1 * 121
        elif c in "a":
            ans += 1 * 42
        elif c in "N":
            ans += 1 * 6
        elif c in "U":
            ans += 1 * 1
    return ans
                            
#################
#Question 2.8
#################


def encrypt(s):
    '''
    (str) -> str
    Preconditions: None
    Returns a string with the encrypted version of s
    '''
    ans = -1
    ans2 = 0
    if len(s)>1 and len(s) != 3:
        newstring = s[ans] + s[ans2]
    
        if len(s)%2 == 0: 
            for x in range(math.floor((len(s)/2)-1)):
            
                while x in range(math.floor((len(s)/2))):
            
                    if x%2 == 0:
                        ans = ans -1
                        ans2 = ans2 +1
                        string = s[ans] + s[ans2]
                
                        break
                    else:
                        ans2 = ans2 +1
                        ans = ans -1
                        string = s[ans] + s[ans2]
           
                        break
                newstring = newstring + string
            print(newstring)
        else:
            for x in range(math.ceil((len(s)/2))):
        
                while x in range(math.ceil(len(s)/2)):
            
                    if x%2 == 0:
                        ans = ans -1
                        
                        string = s[ans]
                
                        break
                    else:
                        ans2 = ans2 +1
                    
                        string = s[ans2]
               
                        break
                newstring = newstring + string
            print(newstring)
        
    elif len(s)<=1:
        newstring = s[ans]
        print(newstring)

    elif len(s) == 3:
        newstring = s[ans] + s[ans2]
        for x in range(math.floor((len(s)/2))):
        
            while x in range(math.floor(len(s)/2)):
            
                if x%2 == 0:
                    ans = ans -1
                        
                    string = s[ans]
                
                    break
                else:
                    ans2 = ans2 +1
                    
                    string = s[ans2]
               
                    break
            newstring = newstring + string 
            print(newstring)

#################
#Question 2.9
#################

def weaveop(s):
    '''
    (str) --> str
    Preconditions: None
    Returns a string with op inserted between consecutive characters. The o and p can be capitalised if the character before or after are capitalised
    '''
    z = ""

    if len(s) == 1:
        z = s
    elif len(s) == 0:
        z = s

    else:
        for x in range(0,len(s)-1):
            z = z+s[x]

            if str.isalpha(s[x]+s[x+1]):
                    if str.islower(s[x]):
                        z = z + "o"
                    else:
                        z = z + "O"
                    if str.islower(s[x+1]):
                        z = z + "p"
                    else:
                        z = z + "P"
        z = z + s[len(s)-1]

    return z

#################
#Question 2.10
#################


def squarefree(s):
    '''
    (str) --> bool
    Precoditions: none
    Returns True if s is squarefree and False if not
    '''

    Truth = True

    for x in range(1,len(s)):
        for y in range(len(s)-1):

            v = s[y:y+x]
            w = s[y+x: y+2*x]

            if v == w:
                Truth = False
    return Truth
