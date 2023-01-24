# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 3
# year 2020
def is_up_monotone(X,d):
    '''
    (string,string) ---> (bool)
    preconditions : X == bool , d== positive int in form of string
    function that tell you if your string is up monotone
    '''
    a=0
    d = int(d)
    Truth = True
    accum = 1
    for i in range(0,len(X),d):
        x = X[i:i+d]
        z = int(x)

        if accum == int(len(X)/d) :
            print(str(x))

        else :
            print(x +",", end=" ")
            accum = accum +1
#PART 2
        if a >= z:
            Truth = False
            a = z
        else :
            a= z

    return Truth
        
# you can add more function definitions here if you like       


            
# main
print("************************************************")
print("*      __Welcome to up-monotone inquiry__      *")
print("************************************************")
name = input("What is your name \t ")

print("************************************************")
print(f"* __{name}, welcome to up-monotone inquiry__  *")
print("************************************************")

flag=True
while flag:
    question=input(name+", would you like to test if a number admits an up-monotone split of given size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
        print("************************************************")
        print(f"*              __Good bye {name}!__             *")
        print("************************************************")
    #YOUR CODE GOES HERE. The next line should be elif or else.

    elif question == 'yes' :
#### FIX FLOAT
        print("Good choice!")
        X = input("Please enter a positive Integer ")
        X = X.strip().lower()
        if X.strip().lower().isdigit() == False :
            if "-" in X.strip().lower():
                print("The Input can only be positive(+). Try again.")
            elif '.'in X.strip().lower():
                print("The Input can only be an integer(no decimals). Try again.")
            else:    
                print("The Input can only contain digits. Try again.")
        elif X == "0" :  
             print("The Input can only be positive(+). Try again.") 
        elif X.strip().lower().isdigit() == True :
                d= input(f"Input the split. The split has to divide the length of {X} i.e. {len(X)}")
                if d.strip().isdigit() == False :
                    print("The Input can only contain digits. Try again.")
                elif len(X.strip()) % int(d.strip()) == 0 or len(X)/ int(d.strip()) ==1 :
                    Truth = is_up_monotone(X,d)
                    if Truth == True :
                        print("The sequence is up-monotonous.")
                    else :
                        print("The sequence is not up-monotonous")
                elif len(X.strip()) % int(d.strip()) != 0 :
                    print(f"{d} does not devide {len(X)}. Try again.")
                elif d.strip() == 0 :
                    print("The Input can only be positive(+). Try again.")
        elif int(X.strip().lower().isdigit()) == 0 :  
             print("The Input can only be positive(+). Try again.")   
    else :
         print("Please input Yes or No. Try again.")
         continue
        
'''
X = input("Please enter a positive Integer ")
        if X.strip().lower()in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.\\ ":
            print("The Input can only contain didgits. Try again.")
        elif X.strip().lower() == type(float):
            print("The Input can only contain didgits. Try again.")
        elif int(X.strip().lower()) <= 0 :
            print("The input has to be a positive(+). Try again")
        elif int(X.strip().lower()) > 0 :
            print("we in")
            pass ########
'''
