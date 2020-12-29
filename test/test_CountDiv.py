from py_code.CountDiv import solution

def test_solution():
    assert solution(6, 11, 2) == 3
    assert solution(12, 18, 3) == 3
    assert solution(0, 20, 4) == 6
    assert solution(10, 10, 5) == 1
    assert solution(10, 10, 7) == 0
    assert solution(10, 10, 20) == 0
    assert solution(11, 345, 17) == 20
    assert solution(1, 1, 11) == 0
    assert solution(11, 13, 2) == 1
    assert solution(101, 123456789, 10000) == 12345
    assert solution(11, 14, 2) == 2