import random
b = []

for i in range(0,99):
    b.append(random.randint(0,9))

a = []
for i in b[::2] :
    a.append(i)
print(f"{b} \n \n \n")
print(a)

