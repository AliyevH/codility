from py_code.MaxProductOfThree import solution

def test_solution():
    
    A = [ -3, 1, 2, -2, 5, 6]
    solution(A) == 60

    A = [-5, 5, -5, 4]
    solution(A) == 125