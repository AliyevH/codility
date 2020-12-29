
def solution(A):
    temp = {}

    for i in A:
        if not temp.get(f"{i}"):
            temp[f"{i}"] = i
        else:
            temp.pop(f"{i}")

    return temp.popitem()[1]



A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))