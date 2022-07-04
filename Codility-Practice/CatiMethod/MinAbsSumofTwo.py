def solution(A):
    S = len(A)
    Min = max(A)*2

    for i in range(0,S):
        for j in range(i,S):
            last = abs(A[i]+A[j])
            if last < Min:
                Min = last
            
    return min 
