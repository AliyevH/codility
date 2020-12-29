from py_code.MinAvgTwoSlice import solution

def test_solution():
    A = [4, 2, 2, 5, 1, 5, 8]
    assert solution(A) == 1

    A = [-3, -5, -8, -4, -10]
    assert solution(A) == 2
