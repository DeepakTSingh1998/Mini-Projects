def solution (A,K):
    B = []
    for i in range(0,K):
        for j in range(0,len(A)):
            B.append(A[j-1])
        
        A = B
        B = []
    
    return A
