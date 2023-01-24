# Family name: Scott Makos
# Student number 
# Course: IT1 1120
# Assignment number 2
#Year: 2020

#Question 1

def min_enclosing_rectangle(radius, x, y):
    '''
    (num, num, num) --> (num,num)
    Precondtion: must input numbers
    Function that returns the bottom left coordinates of a the smallest possible square containing a circle 
    '''
    sqry = y - radius
    sqrx = x - radius
    if radius <=0 :
        return 
    else :
        return(sqrx, sqry)

#Question 2

def vote_percentage(results):
    '''
    (string) --> float
    Precondtion: Only input one string containing "yes", "no" or "abstained"
    Function that returns the percentage of yes votes
    '''
    y = "yes"
    ty = results.count(y)
    n = "no"
    tn = results.count(n)
    return (ty/(tn + ty))

#Question 3

def vote():
    '''
    (none) -- > string
    precondition: Only input one string containing "yes", "no" or "abstained" 
    Fucntion that takes the total votes and determines if the proposal passes unanimously, with super majority or a simple majority
    '''
    votes = input("Enter the yes, no, abstained votes one by one and then press enter: ")
    outcome = vote_percentage(votes)
    if outcome == 1 :
        print("proposal passes unanimously")
    elif outcome >= (2/3) and outcome < 1:
        print("proposal passes with super majority")
    elif outcome >=(1/2) and outcome < (2/3) :
        print("proposal passes with simple majority")
    else :
        print("proposal fails")
