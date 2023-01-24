#############
#Question 1
#############
def indexes(s,n) :
    lit = []
    for i in range(0,len(s)) :
        if n == s[i] :
            lit.append(i)
        else :
            lit = lit
    print(lit)

##############
#Question 2
##############
def doubles(s) :
    for num in range(0,len(s)-1) :
        if 2*s[num] == (s[num+1]) :
            print(s[num+1])
        else :
            continue

##############
#Question 3
##############
def four_letter(L) :
    four =[]
    for word in range(0,len(L)) :
        if len(L[word]) == 4 :
            four.append(L[word])
    print(four)
            
##############
#Question 4
##############
def inBoth(s,m):
    Truth = False
    for item in range(0,len(s)) :
        for n in range(0,len(m)):
            if s[item] == m[n] :
                Truth = True
    return Truth
##############
#Question 5
##############
def intersect(n,m) :
    mommy = []
    for i in range(0,len(n)) :
        if n[i] in m :
            mommy.append(n[i])
    print(mommy)
##############
#Question 6
##############
