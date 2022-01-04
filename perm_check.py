# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    A.sort()
    for index, element in enumerate(A):
        if index+1 != element:
            return 0
    return 1
