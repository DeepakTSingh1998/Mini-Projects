def solution(D):    
    M = 0
    for i in range(1,D+1):
        if D % i == 0:
            M += 1
    
    return M
