# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 4
# year 2020

def number_divisible() :
    '''
    List of int, int ->None
    Preconditions : lst and x can not be float or string
    This function returns which integers in a list can be divided by the integer in the second parameter
    '''
    lst = input("Please input a list of numbers separated by spaces : ").strip().split()
    x = input("Please input an integer: ").strip()
    new = []
    accum = 0
    for i in lst :
          new.append(int(i))
    for i in new :
        if i % int(x) == 0 :
            accum += 1
    print(f"The number of elements divisible by {x} is {accum}.")

number_divisible()
