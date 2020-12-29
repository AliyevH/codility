def solution(A: list):
    A.sort()
    
    min = 1

    for i in A:
        if i == min:
            min += 1
        elif i != min:
            return 0

    return 1
print(solution([4,1,3]))