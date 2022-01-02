# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    A.sort()
    first = A.pop(0)
    check_pair = True
    for second in A:
        if check_pair: 
            if first != second:
                break 
            check_pair = False
        else:
            check_pair = True
        first = second
    
    return first

