# https://app.codility.com/programmers/lessons/6-sorting/triangle

def solution(A):
    A.sort()
    for idx in range(1, len(A)-1):
        if A[idx-1] + A[idx] > A[idx+1] and A[idx-1] + A[idx+1] > A[idx] and A[idx] + A[idx+1] > A[idx-1]:
            return 1
    return 0
