def solution(A):
  A = [10,2,5,1,8,12]
  counter = 0

  for i in range(0,len(A)-2):
      for j in range(1+i,len(A)-1):
          for k in range(1+j,len(A)):
              if ((A[i]+A[j]>A[k]) and
                (A[j]+A[k]>A[i]) and
                (A[k]+A[i]>A[j])):
                      counter += 1
  return counter 
                    
                   
