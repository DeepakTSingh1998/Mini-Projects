def solution (X,Y,D):
    jumps = 0
    while X < Y:
        X = D + X
        jumps += 1
    return jumps
    
