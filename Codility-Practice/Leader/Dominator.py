def solution (A):
    Unique = {}
    current = 0
    for i in A:
        if str(i) in Unique:
            Unique[str(i)]['Counter'] += 1
            Unique[str(i)]['location'].append(current)
        else:
            Unique[str(i)]= {'Counter':1,'location':[current]}
        current += 1
    
    for i in Unique:
        if float(Unique[i]['Counter']) >= len(A)/2:
            ans = Unique[i]['location']
            break
        else:
            ans = -1
        
    return ans
        
    
    
