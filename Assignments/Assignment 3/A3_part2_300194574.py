

###############
# Question 2.1
###############

def sum_odd_divisors(n):
    '''
    (int) --> None or int
    Preconditions: None
    Function that takes the number n and returns the sum of all its positive odd divisors
    '''
    
    Sum = 0
    if n == 0:
        return None
    else:
        for x in range(1,(abs(n)+1),2):
            if abs(n)%x == 0:
                Sum = Sum + x
        print(Sum)


###############
# Question 2.2
###############

def series_sum() :
    '''
    (None) --> number
    Precondtion: n =! negative
    Functions that returns the sum of the following series 1000 + 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^2
    '''

    n = int(input("Please enter a positive integer"))
    if n < 0 :
        return None
    else :
        Sum = 0
        for i in range(1,(n+1)) :
            Sum += ((1)/(i**2))
        return 1000 + Sum

###############
# Question 2.3
###############

def pell(n):
    '''
    (int) ---> int
    Preconditions: n >= 0
    Returns the pell number of n
    '''
    x1 = 1
    x2 = 0
    
    if n < 0:
        return None
    elif n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        for x in range(n-1):
            ans = x1*2  + x2
            x2 = x1
            x1 = ans


    return ans


###############
# Question 2.4
###############

def countMembers(s):
    '''
    (str) ---> int
    Preconditions: Must input a str
    Function that returns the number of items in s that are extroadinary
    '''
    accum = 0
    for chara in s :
        if chara in '23456efghijkFGHIJKLMNOPQRSTUVWX,\!' :
            accum += 1
    return accum

###############
# Question 2.5
###############

def casual_number(s):
    '''
    (str) --> int
    Preconditions: Must input a string
    Function that takes the string s and returns an int representing the monetary value of the numbers in that string
    '''
    x = ""
    if "-" in s :
       neg = -1
    else :
        neg = 1
    ###
    if s.count('-')> 1 :
        return None
    ###
    for char in s :
         if char in "abcdefghijklmnopqrstuvwxyzx" :
            return None 
         elif char =="," :
            x= x+char.replace(",","")
         elif char in "1234567890" :
            x = x+char
    ###
    if x == "" :
        return None
    else :
        return (neg *int(x))

##############
#Question 2.6
##############

def alienNumbers(s):
    '''
    (str) ---> int
    Precondition: You must insert a string containing the symbols to convert
    Function that turns the symbols to decode in the string and converts them into numbers and sums them up
    '''
    a = s.count("T")
    b = s.count("y")
    c = s.count("!")
    d = s.count("a")
    e = s.count("N")
    f = s.count("U")
    Sum = (a*1024)+(b*598)+(c*121)+(d*42)+(e*6)+(f*1)
    return Sum

##############
#Question 2.7
##############

def alienNumbersAgain(s):
    '''
    (str) ---> int
    Precondition: You must insert a string containing the symbols to convert
    Function that turns the symbols to decode in the string and converts them into numbers and sums them up
    '''
    res = 0
    for c in s :
        if c in "T":
            res += 1 * 1024
        elif c in "y":
            res += 1 * 598
        elif c in "!":
            res += 1 * 121
        elif c in "a":
            res += 1 * 42
        elif c in "N":
            res += 1 * 6
        elif c in "U":
            res += 1 * 1
    return res 

###############
# Question 2.8
###############
def encrypt(s):
    '''
    (str)--> str
    Preconditions: None
    Returns a string of the encrypted version of the string s
    '''

    Str = ''

    for x in range(1, int(len(s)/2)+1):
        Str = Str + s[-x]+s[x-1]

    if len(s) % 2 == 1:
        Str = Str + s[int(len(s)/2)]

    return Str


###############
# Question 2.9
###############

def weaveop(s):
    '''
    (str) --> str
    Preconditions: None
    Returns a string with the letter o and p inserted between consecutive characters. 
    '''
    Str = ""

    if len(s) == 1:
        Str = s
    elif len(s) == 0:
        Str = s

    else:
        for x in range(0,len(s)-1):
            Str = Str+s[x]

            if str.isalpha(s[x]+s[x+1]):
                    if str.islower(s[x]):
                        Str = Str + "o"
                    else:
                        Str = Str + "O"
                    if str.islower(s[x+1]):
                        Str = Str + "p"
                    else:
                        Str = Str + "P"
        Str = Str + s[len(s)-1]

    return Str


###############
#Question 2.10
###############


def squarefree(s):
    '''
    (str) --> bool
    Precoditions: none
    Returns True if s is squarefree and False if it isn't
    '''
    Bool = True
    

    for x in range(1,len(s)):
        for y in range(len(s)-1):

            v = s[y:y+x]
            w = s[y+x: y+x*2]

            if v == w:
                Bool = False
    return Bool
