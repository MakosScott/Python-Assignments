# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 6
# year 2020
import string

def open_file():
    '''N
    one->file object
    preconditions : None    
    Keeps asking for a file name until u input a proper file name. it then returns a string version of the file'''
    file = None
    while file == None:
        while file == None :
            try :
                file = input("Please input the name of the file you wish to open")
                file = file.strip()
                b = open(file)
                b.close()
            except FileNotFoundError :
                print("There is not file with that name. Please Try again")
                file = None
        return file
    
def read_file(fp):
    d = {}
    lst = []
    newtxt = cleantxt()
    '''
    (file object)->dict
    preconditions : None
    makes each word a key in a dictionary. The values associated with each key is the number of the line where you can find the word
    '''


    newtxt = newtxt.splitlines()

    for i in range(0,len(newtxt)):
        temp = newtxt[i].split()
        for word in temp :
            if len(word) >= 2 :
                if word not in d:
                   d[word] = {i+1}
                else :
                    d[word].add(i+1)
    
    return d

def find_coexistance(d, query):
    '''
    (dict,str)->list
    Preconditions : query has to be a string of words seperated by blank spaces 
    If query is one word this function returns a sorted list of the lines number in which that word can be found. If there are more than one word in query, the function returns the lines that each word have in common
    '''
    # YOUR CODE GOES HERE
    
    check = []
    query = query.split()
    nums=[]
    x = []
    a= {}
    if len(query) == 1 :
        x = d[query[0]]  
    elif len(query) > 1 :
        for ele in range(0,len(query)-1) :
            a= d[query[ele]].intersection(d[query[ele+1]])
            for i in a :
                if i not in x :
                    x.append(int(i))
              
    
    return sorted(x)

###################      
#helper functions
####################

def wordcheck(d,query) :
    '''
    (dictionary,string)-> Bool
    preconditions : query has to be a string of words seperated by blank spaces 
    checks if each word in query is in the dictionary. Returns true if all words are in the dictionary. returns False and prints "The word '"+word+"' not in the file" if the word doesnt exist in the dictionary
    '''
    condition2 = True
    if query == "":
            print(f"the word '' not in the file")
            condition2 = False

    if len(query) == 1 :
        if query not in d :
            print(f"The word '"+query+"' not in the file")
            condition2 = False
            
    elif len(query) >1 :
        query = query.split()
        for word in query :
            if word not in d :
                print(f"The word '"+word+"' not in the file")
                condition2 = False
                break
    return condition2
    
def cleantxt() :
    '''
    None -> string
    Preconditions : None
    Returns a string version of the textfile without any non-letters
    '''
    
    txt = open(file).read().lower()
    newtxt = ""
    for chara in txt :
        if chara not in "abcdefghijklmnopqrstuvwxyz \n " :
            newtxt = newtxt
        else :
            newtxt += chara
    return newtxt

def convert(h) :
    '''list -> string
    Preconditions : h has to be a list of numbers
    Returns a string with all the elements of list seperated by a space
    '''
    x = ""
    for i in h :
        x += f"{i} "
        
    return x

    
    
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# YOUR CODE GOES HERE
h = None
while query != "q" :
    t = wordcheck(d,query)
    if t == True :
        h = find_coexistance(d, query)
        if len(h)== 0 :
            h = convert(h)
            print(f"The one or more words you entered does not coexist in a same line of the file.")
        else :
            h = convert(h)
            print(f"The one or more words you entered coexisted in the following lines of the file: \n{h}")
    else :
        print
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
  
        
    













'''
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
'''

'''
    txt = open(file).read().lower()
    newtxt = ""
    for chara in txt :
        if chara not in "abcdefghijklmnopqrstuvwxyz \n " :
            newtxt = newtxt
        else :
            newtxt += chara
'''
