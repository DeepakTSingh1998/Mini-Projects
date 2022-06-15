def solution (A):
    
    Distinct_Values = []
    for i in range(0,len(A)):
        if len(Distinct_Values) > 0:
            for j in range(0,len(Distinct_Values)):
                if A[i] not in Distinct_Values:
                    Distinct_Values.append(A[i])
                
        else:
            Distinct_Values.append(A[i])
    
    Distinct_sum = len(Distinct_Values)
    return Distinct_sum 
