def solution (A):
    maximum = 0
    for i in range(2,len(A)):
        for j in range(0,len(A)-i):
            P = A[(i-2)]
            Q = A[(i-2)+j+1]
            R = A[(i-2)+j+2]
            value = P*Q*R
            if value > maximum:
                maximum = value
    
    return maximum
