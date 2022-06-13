def solution (A):
    Ticker =[False for i in range(len(A))]
    for i in range(0,len(A)):
        if A[i] in range(0,len(A)+1):
            Ticker[A[i]-1] = True
        
        if sum(Ticker) == len(A):
            output = 1
            break 
        else:
            output = 0
            
    return output
