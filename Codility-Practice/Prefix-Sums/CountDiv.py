def solution (A,B,K):
    Div_counter = 0
    for i in range(A,B+1):
        Divider = i % K
        if Divider == 0:
            Div_counter += 1
           
    return Div_counter
        
