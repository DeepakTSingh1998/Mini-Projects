def solution (N):
    
    counter = 0
    while True:
        if counter == 0:
            if (N[-1] != N[0] + len(N) - 1) and (N[-2] != N[-1]-1):
                missing = N[-2] + 1
                break
            else:
                missing = N[1] - 1
        
        
        else: 
            if N[counter] != N[counter-1] + 1:
                missing = N[counter-1] + 1
                break
    
        counter += 1
    
    return missing
    
