def solution (A):
    Tot_pairs = int((len(A)*(len(A)-1))/2)
    Current_pairs = 0
    passing_pairs = 0
    required_pairs = len(A)
    while Tot_pairs > Current_pairs:
        for i in range(0,len(A)-1):
            loop_pairs = 0
            required_pairs = len(A) - (i+1)
            while required_pairs > loop_pairs:
                array = [A[0+i],A[loop_pairs+1+i]]
                if array == [0,1]:
                    passing_pairs += 1
                
                loop_pairs += 1
                Current_pairs += 1
            
                if passing_pairs > 1000000:
                    output = -1
                    return output
                
                
    return passing_pairs
            
