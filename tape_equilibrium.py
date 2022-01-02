# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    sum_left = A[0]
    sum_right = sum(A[1:])
    minimal_diff = abs(sum_left - sum_right)

    for element in A[1:-1]: #we must stop before last el, P<N
        sum_left = sum_left + element
        sum_right = sum_right - element
        if minimal_diff > abs(sum_left-sum_right):
            minimal_diff = abs(sum_left-sum_right)
    return minimal_diff
