s = '''It was the best of times, it was the worst of times;
it was the age of wisdom, it was the age of foolishness;
it was the epoch of belief, it was the epoch of incredulity;
it was ...'''

#a)
newS = s.replace(",", " " ).replace(".", " ").replace(";"," ").replace("\n", " ")
#b)
newS = newS.strip()
#c)
newS = newS.lower()
#d)
#for "it was" in newS :
   # x = x+1
 #   print(x)
#e)
newS = newS.replace("was","is")
