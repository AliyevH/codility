def solution(A):
    A.sort()
    max = 0
    for i in range(len(A) - 1):
        if A[i] > 0:
            break
        mult = A[i] * A[i + 1]
        if mult > 0:
            if mult > max:
                max = mult

    max1 = max * A[-1]
    max2 = A[-1] * A[-2] * A[-3]
    if max1 > max2:
        return max1
    else:
        return max2