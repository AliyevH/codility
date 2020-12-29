def solution(A, K):
    if not A:
       return []
    
    if sum(A) / len(A) == A[0]:
        return A

    for i in range(K):
        temp = A.pop(-1)
        A.insert(0, temp)
    return A