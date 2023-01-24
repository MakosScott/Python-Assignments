# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 4
# year 2020

def two_lenght_run() :
    '''
    list of numbers -> None
    Preconditions : run has to be a list of integers, so no strings.
    This function tells the user if ther is a run in the list of numbers inputted.
    '''
    truth = False
    run = input("Please input a list of numbers separated by space: ").strip().split()
    x = []
    for i in run :
        x.append(float(i))
    for a in range(0,len(x)-1) :
        if x[a] == (x[a+1]):
            truth = True
    print(truth)
    return truth

two_lenght_run()        


