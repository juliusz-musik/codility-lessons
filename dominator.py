# https://app.codility.com/programmers/lessons/8-leader/dominator

from collections import namedtuple

MaxCount = namedtuple('MaxCount', ('index', 'value'))

def solution(A):
    counts = {}
    max_count = MaxCount(-1, 0)
    for index, number in enumerate(A):
        counts[number] = counts.get(number, 0) + 1
        if counts[number] > max_count.value:
            max_count = MaxCount(index, counts[number])

    result = max_count.index if max_count.value > len(A)/2 else -1
    return result
