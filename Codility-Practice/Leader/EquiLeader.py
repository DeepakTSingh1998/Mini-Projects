def solution (A):
    
    Temp = []
    Equi = 0
    for i in range(0,len(A)-1):
        Temp.append(A[0])
        del A[0]
    
        Unique_Temp = {}
        Unique_A = {}
    
        for i in Temp:
            if str(i) in Unique_Temp:
                Unique_Temp[str(i)]['Counter'] += 1
            else:
                Unique_Temp[str(i)]= {'Counter':1}
    
        for i in A:
            if str(i) in Unique_A:
                Unique_A[str(i)]['Counter'] += 1
            else:
                Unique_A[str(i)]= {'Counter':1}
            
        Temp_biggest = 0      
    
        for i in Unique_Temp:
            if float(Unique_Temp[i]['Counter']) > Temp_biggest:
                Temp_biggest = float(Unique_Temp[i]['Counter'])
                Temp_most = int(i)
            elif float(Unique_Temp[i]['Counter']) == Temp_biggest:
                Temp_biggest = float(Unique_Temp[i]['Counter'])
                Temp_most = False
                
        A_biggest = 0        
    
        for i in Unique_A:
            if float(Unique_A[i]['Counter']) > A_biggest:
                A_biggest = float(Unique_A[i]['Counter'])
                A_most = int(i)
            elif float(Unique_A[i]['Counter']) == A_biggest:
                A_biggest = float(Unique_A[i]['Counter'])
                A_most = False
            
        if Temp_most == A_most:
            Equi += 1
            
    return Equi
    
            
