from py_code.MissingInteger import solution

def test_solution():
    A = []
    assert solution(A) == 1

    A = [-4]
    assert solution(A) == 1

    A = [0]
    assert solution(A) == 1

    A = [1]
    assert solution(A) == 2

    A = [2]
    assert solution(A) == 1

    A = [3]
    assert solution(A) == 1

    A = [1, 2, 3]
    assert solution(A) == 4

    A = [99]
    assert solution(A) == 1

    A = [1, 3, 6, 4, 1, 2]
    assert solution(A) == 5

    A = [-1, -3]
    assert solution(A) == 1

    A = [-1, -2]
    assert solution(A) == 1
    
    A = [i for i in range(0, 101)]
    assert solution(A) == 101

    A = [i for i in range(102, 200)]
    assert solution(A) == 1

    A = [90, 91, 92, 93]
    assert solution(A) == 1