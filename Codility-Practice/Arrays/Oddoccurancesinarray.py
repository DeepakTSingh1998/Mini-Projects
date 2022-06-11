def solution (A):
    n = 1
    while True:
        pair1 = A[0]
        pair2 = A[n]
        if pair1 == pair2:
            del A[0]
            del A[n-1]
            n = 1
            if len(A) == 1:
                odd = A[0] 
                break
        else:
            n = n + 1
            if len(A) == n:
                odd = A[0]
                break
    return odd
                    
