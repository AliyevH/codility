from py_code.bitwiseOperation import solution

def test_solution():
    A = [3, 2 ,10 ,6, 3]
    assert solution(A) == 4

    A = [13, 7, 2, 8 ,3]
    assert solution(A) == 3

    A = [1, 2, 4, 8]
    assert solution(A) == 1

    A = [16, 16]
    assert solution(A) == 2

    A = [1, 3, 7, 2, 8]
    assert solution(A) == 2