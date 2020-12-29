
def solution(A: int, B: int, K: int):
   
    counter = 0

    a = int(A / K)
    b = int(B / K)

    if A % K == 0:
       counter += 1
    
    return b - a + counter



print(solution(10, 10, 7))