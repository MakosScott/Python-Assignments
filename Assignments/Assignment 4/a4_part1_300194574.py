# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 4
# year 2020
def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    x = ''
    for char in word :
        if char in "!.?:,'-_\/()[]{}%0123456789" :
            x = x
        elif char in '"' :
            x = x
        else :
            x = x +char
    x = x.lower()
    
    return x
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
   

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''
    w1 = sorted(w1)
    w2 = sorted(w2)
    return w1==w2
    
        
    
def create_clean_sorted_nodupicates_list(s):
    s = clean_word(s)
    text1 =[]
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', , 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''
    
    #YOUR CODE GOES HERE
    s = s.split()
    for word in s :
        if word not in text1:
            text1.append(word)
    text1.sort()
    return text1
            
    pass

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
    #YOUR CODE GOES HERE
    anas = []
    for i in range(0,len(wordbook)) :
        w1 = word
        w2 = wordbook[i]
        test_letters(w1, w2)
        if test_letters(w1, w2) == True :
            anas.append(wordbook[i])
        elif test_letters(w1, w2) == False :
            anas = anas
    for i in anas :
        if i == word :
            anas.remove(word)
        else :
            anas = anas
            
    return sorted(anas)
            
        
        

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''
    
    #YOUR CODE GOES HERE
    count =[]
    for i in range(0,len(l)) :
        h = word_anagrams(l[i], wordbook)
        count.append(len(h))
    return count


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''
    #YOUR CODE GOES HERE
    k_ana = []
    for num in range(0,len(l)) :
        if anagcount[num] == k :
            k_ana.append(l[num])
        else :
            k_ana = k_ana
    return sorted(k_ana)
                
                
def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''
    Max = 0
    Maxlist = []
    for num in range(0,len(anagcount)):
        if anagcount[num] > Max :
            Max = anagcount[num]
        else :
            Max = Max
    for num in range(0,len(anagcount)) :
        if anagcount[num] == Max :
            Maxlist.append(l[num])
        else :
            Maxlist = Maxlist
    return sorted(Maxlist)

    
    
    #YOUR CODE GOES HERE
    pass

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    #YOUR CODE GOES HERE
    zerolist = []
    for num in range(0,len(anagcount)):
        if anagcount[num] == 0 :
            zerolist.append(l[num])
        else :
            zerolist = zerolist
    return sorted(zerolist)
    
            




    
##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

if choice=='1':
    # YOUR CODE GOES HERE
    # when asking for k from the user you may assume that they will enter non-negative integer
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)
    Maxlist = max_anagram(l, anagcount)
    print(f"\nOf all the words in your file, the following words have the most anagrams: {Maxlist}")
    print("\n \nHere are their anagrams : ")
    for word in Maxlist :
        print(f"The anagrams for {word} are  :{word_anagrams(word, wordbook)}")
    Zero = zero_anagram(l, anagcount)
    print(f"\nHere are the words from your file that have no anagrams : {Zero}")
    k = int(input("\nPlease enter an positive integer so we can determine which words have that many anagrams : "))
    last = k_anagram(l, anagcount, k)
    print(f"\nHere are the words that have exactly {k} anagrams : {last}")

elif choice=='2':
    #YOUR CODE GOES HERE
    hlp = input("Please enter the letters you posses, one after another with no space : ")
    while " " in hlp :
            print("Error you added space(s). Try again. ")
            hlp = input("Please enter the letters you posses, one after another with no space : ")
    
    choice2 = input("Would you like help forming words with : \n1.All these letters \n2.All these letters but one. ")
    while choice2.strip() !=  "1" and choice2.strip() !="2":
        choice2 = input("That is not a valid input. Please pick 1 or 2 : ")


    if choice2 == "1" :
        print(f"The letters you gave us are : {hlp}")
        word= hlp
        z = word_anagrams(word, wordbook)
        if word in wordbook :
            z.append(word)
        if z == [] :
            print("There are no words that can be made with these letters")
        else :
            print("Here are the words we can form with these letters : ") 
            print(sorted(z))
        
    elif choice == "2" :
        word = ""
        print(f"The letters you gave us are : {hlp} \nLet's see what we get if we ommit one of these letters.\n")
        word =""
        for i in range(0,len(hlp)) :
            word = hlp[:i]+hlp[i+1:]
            print(f"Without the letter in position {i+1} we have the letters : {word} ")
            u = word_anagrams(word, wordbook)
            if word in wordbook :
                u.append(word)
            if u == [] :
                print("There are no words you can make with these letters.\n")
            else :
                print(f"With theses letters you can make the words :\n{u}\n")
                       
                  
else:
    print("Good bye")


