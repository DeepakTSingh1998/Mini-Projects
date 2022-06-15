def solution (A):
    biggest = 0
    for i in range(0,len(A)):
        for j in range(1+i,len(A)+1):
            value = sum(A[i:j])
            if value > biggest:
                biggest = value
                
            
        
