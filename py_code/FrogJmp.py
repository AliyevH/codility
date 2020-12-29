from math import ceil
def solution(X, Y, D):
    current_point = X
    end_point = Y
    jumps = D
    jump_count = 0

    return ceil((end_point - current_point) / jumps)



x = 10
y = 85
d = 30

print(solution(x, y, d))