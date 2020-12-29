def solution(A):
    lenght = len(A)

    min_index = 0  
    min_average = (A[0] + A[1]) / 2

    for i in range(0, lenght - 2):
        current_average_2 = (A[i] + A[i+1]) / 2
        current_average_3 = (A[i] + A[i+1] + A[i+2])  / 3
        
        if current_average_2 < min_average:
            min_index = i
            min_average = current_average_2
        
        if current_average_3 < min_average:
            min_index = i
            min_average = current_average_3

    return min_index


A = [-3, -5, -8, -4, -10]

print(solution(A))