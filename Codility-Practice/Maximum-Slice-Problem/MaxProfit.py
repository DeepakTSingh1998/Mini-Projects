def solution (A):
    biggest = 0
    for i in range(0,len(A)-1):
        for j in range(1+i,len(A)):
            value = A[j] - A[i]
            if value > biggest:
                biggest = value
    return biggest
        
