# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 4
# year 2020

def longest_run() :
    '''
    list of numbers -> None
    preconditions : variable run has to be a string of multiple numbers seperated by a space
    This function tells you the lenght of the longest run
    '''
    truth = False
    highest = 0
    accum = 0
    run = input("Please input a list of numbers separated by space: ").strip().split()
    x = []
    for i in run :
        x.append(float(i))
 
    for a in range(0,len(x)-1) :
        if x[a] == (x[a+1]):
             accum += 1
             if highest < accum :
                 highest = accum
        elif x[a] != (x[a+1]):
            accum = 0

    extra = len(run)
    if extra == 0 :
        highest = highest
    else :
        highest = highest +1
    
    print(highest)
    return highest

longest_run()
