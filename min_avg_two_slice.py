# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice

from statistics import mean

def solution(A):
    prefix_2, prefix_3 = [],[]

    prefix_2.append((A[1]+A[0])/2)
    for ind in range(2, len(A)):
        prefix_2.append((A[ind]+A[ind-1])/2)
        prefix_3.append((A[ind]+A[ind-1]+A[ind-2])/3)

    if prefix_3 and min(prefix_2) > min(prefix_3):
        return prefix_3.index(min(prefix_3))
    return prefix_2.index(min(prefix_2))
