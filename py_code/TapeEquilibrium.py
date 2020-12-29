def solution(A):
    minimum_difference = 0
    length = len(A)
    sum_val = sum(A)
    left_sum = 0

    if not length:
        return minimum_difference

    for i in range(0, length-1):
        left_sum += A[i]
        estimate = sum_val - left_sum
        current_differemce = abs(left_sum - estimate)
        print("left_sum: ", left_sum)
        print("estimate: ", estimate)
        print("current_differemce: ", current_differemce)
        print("\n")

        if i == 0 or current_differemce < minimum_difference:
            minimum_difference = current_differemce 

    return minimum_difference

A = [1, 2]
print(solution(A))