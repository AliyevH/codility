from itertools import permutations

def solution(A):
    A.sort(reverse=True)

    and_operation_count = 0

    if len(A) == 2:
        if A[0] & A[1] > 0:
            return 2

    for i in range(len(A) - 1):
        if A[i] & A[i+1] > 0:
            and_operation_count += 1

    if and_operation_count == 0:
        return 1
    return and_operation_count



# A = [1, 3, 7, 2, 8]
# solution(A)


import random
from time import time

randomlist = []

for i in range(100000):
    n = random.randint(-1000000, 1000000)
    randomlist.append(n)

start = time()
print(solution(randomlist))
print("Finished in: ", time() - start)
