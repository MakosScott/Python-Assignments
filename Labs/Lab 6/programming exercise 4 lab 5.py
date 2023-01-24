def sum_5_consecutive(x) :
    truth = False
    if len(x) < 5 :
        return False
    else :
        for i in range(0,len(x)):
            if int((i+4)) >= len(x) :
                break
            elif (x[i] + x[i+1] + x[i+2] +x[i+3] +x[i+4]) == 0 :
                truth = True
                break
            elif (x[i] + x[i+1] + x[i+2] +x[i+3] +x[i+4]) != 0 :
                truth = False
            
    return truth
            
