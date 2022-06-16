def solution (A):
    
    Non = [0 for x in range(len(A))]
    counter = 0
    for i in A: 
        Temp = A.copy()
        del Temp[counter]
        for j in Temp:
            if i % j != 0:
                Non[counter] += 1
            
        counter += 1
    return Non
