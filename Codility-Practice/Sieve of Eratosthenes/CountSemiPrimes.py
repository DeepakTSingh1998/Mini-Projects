def solution(P,Q,N):
    def prime(n):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    Primes = []
    Semi = []
    for i in range(2,N):
        if prime(i) == True:
            Primes.append(i)
    for i in range(0,len(Primes)):
        for j in range(0+i,len(Primes)):
            Semi.append(Primes[i]*Primes[j])

    Semi.sort()
    Range = []
    Output = []
    for j in range(0,len(P)):
        for i in range(0,len(Semi)):
            if Semi[i] >= P[j] and Semi[i] <= Q[j]:
                Range.append(True)
            else:
                Range.append(False)
            
        Output.append(sum(Range))
        Range = []
        
    return Output
