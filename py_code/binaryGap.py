import re
def solution(n):
    binary_number = bin(n)[2:]
    max_gap = 0
    while re.findall("[1]+[0]+[1]", binary_number):
        x = re.findall("[1]+[0]+[1]", binary_number)        
        binary_number = binary_number[len(x[0])-1:]

        if max_gap < x[0].count("0"):
            max_gap = x[0].count("0")
    return max_gap


print(solution(1041))
