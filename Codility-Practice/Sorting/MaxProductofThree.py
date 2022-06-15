def solution (A):
    A.sort()
    N = len(A)
    max = A[N-1]*A[N-2]*A[N-3]
    return max
