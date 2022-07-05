def solution(A, B):
    if (len(A) < 2) or (len(B) < 2):      
        return len(A)
    counter = 0       
    intial_B = B[0]
    i = 1       
    while i < len(A):
        counter += 1
        while i < len(A) and A[i] <= intial_B:   
            i += 1
        if i == len(A):                         
            break
        intial_B = B[i]
    return counter
    
    A = [1,3,7,9,9]
    B = [5,6,8,9,10]
    
    print(solution(A,B))
