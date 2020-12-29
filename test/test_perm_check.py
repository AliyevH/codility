from py_code.PermCheck import solution

def test_solution():
    is_permutation = True
    not_permutation = False

    A = [4, 1, 3, 2]
    assert solution(A) == is_permutation

    A = [4, 1, 3]
    assert solution(A) == not_permutation

    A = [30, 31, 32, 33, 34]
    assert solution(A) == is_permutation

    A = [-30, -31, -32, -33, -34]
    assert solution(A) == is_permutation

    A = [2,3]
    assert solution(A) == is_permutation

    A = [2]
    assert solution(A) == not_permutation

    A = [3, 2]
    assert solution(A) == not_permutation
