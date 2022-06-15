def solution(A):
    biggest = 0
    for x in range(0,len(A)-2):
        for y in range(1+x,len(A)-1):
            for z in range(1+y,len(A)):
                value = sum(A[x+1:y]) +  sum(A[y+1:z])
                if value > biggest:
                    biggest = value
                    
    return biggest
