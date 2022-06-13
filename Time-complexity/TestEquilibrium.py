def solution(A):
    P = []
    first = 0
    last = sum(A)
    for i in range(0, len(A)-1):
        first += A[i]
        last -= A[i]
        P.append(abs(first-last))
    
    min_dif = min(P)
    return min_dif
    
