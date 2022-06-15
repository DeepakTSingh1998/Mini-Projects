def solution (A):
    smallest_value = max(A)
    for i in range(1,len(A)):
        last = len(A) - i
        for j in range(0,last):
            value = 0
            for k in range(j,last+1):
                value += A[k]
            div_value = value/(last-j+1)
            if div_value < smallest_value:
                smallest_start = j
                smallest_value = div_value
    
    return smallest_start
