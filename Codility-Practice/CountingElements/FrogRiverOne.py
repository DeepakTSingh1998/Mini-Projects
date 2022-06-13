def solution (A,X):
    
    Ticker =[[False for x in range(1)] for y in range(X)]
    K = 0
    n = 0

    for i in range(0,len(A)):
        if A[i] in range(1,X+1):
            Ticker[A[i]-1] = True
        
        try:
            if sum(Ticker) == X:
                break
        
        except:
            n += 1
                
        K += 1
    
    return K
