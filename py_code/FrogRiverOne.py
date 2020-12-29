def solution(X, A):
    all_nums = {}

    sum = (X**2 + X) / 2
    counter = 0

    length = len(A)

    if length == 1 and A[0] == X:
        return 0

    for i in range(length):

        if sum > 0 and not all_nums.get(A[i]):
            sum -= A[i]
            all_nums[A[i]] = A[i]

        if sum == 0:
            return i      

    return -1



A = [5]

X = 5
print(solution(X, A))

