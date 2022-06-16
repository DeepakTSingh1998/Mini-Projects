def solution(N):    
    M = 0
    P_min = 2*(N+1)
    for i in range(1,N+1):
        if N % i == 0:
            N_new = int(N/i)
            M += 1
            P = 2*(N_new+i)
            if P < P_min:
                P_min = P
    return P_min
