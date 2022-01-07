# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div

def solution(A, B, K):
    if A%K == 0:
        result = B//K-(A-1)//K
    else:
        result = B//K-A//K
    return result
