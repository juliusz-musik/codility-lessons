# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem

def solution(A):
    A.sort()
    for index, elem in enumerate(A):
        if index+1 != elem:
            return index+1
    #N+1 element is missing
    return len(A)+1

