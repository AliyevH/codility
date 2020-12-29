def solution(A):
    global pairs

    length = len(A)
    
    
    if length == 1:
        return 0
    
    pairs = 0
    counter = 0
    for i in A:
        if i == 0:
            pairs += 1
        if i == 1:
            counter += pairs

    if counter > 1000000000:
        return -1 
    return counter

A = [0, 0]
solution(A)
