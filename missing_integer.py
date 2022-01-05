# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer

def solution(A):
    numbers = set(A)
    for number in range(1, len(numbers)+1):
        if number not in numbers:
            return number
    return number+1
