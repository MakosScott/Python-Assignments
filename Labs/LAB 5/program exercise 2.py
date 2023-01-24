num =0
Sum =0
for i in range(1,10000):
    num = num+1
    if num %i == 0 :
        Sum += i
        if Sum == i:
            print(f" {num} is a perfect number")
        
    
