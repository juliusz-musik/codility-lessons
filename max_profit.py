# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

def solution(A):
    if not A:
        return 0

    max_profit = 0
    min_value = A[0]
    for a in A:
        if a < min_value:
            min_value = a
        max_profit = max(max_profit, a - min_value)

    return max_profit
