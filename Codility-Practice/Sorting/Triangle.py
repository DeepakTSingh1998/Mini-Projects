def solution (A):
    A.sort()
    N = len(A)
    output = 0
    for i in range(N-2):
        if A[i] > A[i+2] - A[i+1]:
            output = 1
            break
        
    return output
