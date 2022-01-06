# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):
    right = 0 # east
    left = 1 # west

    left_count = A.count(left)
    passes = 0
    for car in A:
        if car == right:
            passes=passes+left_count
        else:
            left_count=left_count-1
        
        if passes > 1000000000:
            return -1
        
    return passes
