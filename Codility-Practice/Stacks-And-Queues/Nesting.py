def solution (S):
    Dict = {
        '(':0,
        ')':0
    }
    

    for i in range(0,len(S)):
        if S[i] in Dict:
            Dict[S[i]] += 1
        
    if (Dict['('] == Dict[')']):
        if S[0] == ')':
            output = 0
        else:
            output = 1
    else: 
        output = 0
        
    return output
