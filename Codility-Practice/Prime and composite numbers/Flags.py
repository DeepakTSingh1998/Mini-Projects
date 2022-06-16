A = [1,5,3,4,3,4,1,2,3,4,6,2]
Peaks = []
for i in range(0,len(A)-2):
    if A[i+1] > (A[i] and A[i+2]):
        Peaks.append(i+1)
        
K = 3
init_pos = 0
while init_pos > len(A) and K > 0:
    if Peaks[init_pos]:
        K -= 1
        init_pos += K
    else:
        init_pos  += 1

            
            
