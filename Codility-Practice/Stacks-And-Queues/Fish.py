def solution (A,B):
    
    last = len(A)-1
    current = 1
    while True:
        if [B[current-1],B[current]] == [1,0]:
            if A[current-1] > A[current]:
                del A[current]
                del B[current]
            
            else:
                del A[current-1]
                del B[current-1]
        
            last -= 1
        else:
            current += 1
    
        if current > last:
            break
    
    return len(A)
