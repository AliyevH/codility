def solution(A):
    if len(A) >= 1:
        x = [i for i in range(1, len(A) + 2)]
        return sum(x) - sum(A)
    if len(A) == 1:
        return A[0]
    return 1


A = []

print(solution(A))