# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):
    try:
        rotations = K % len(A)
    except ZeroDivisionError:
        return A

    if rotations:
        return A[-rotations:]+A[:len(A)-rotations]
    else:
        return A
