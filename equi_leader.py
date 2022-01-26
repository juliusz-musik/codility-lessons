# https://app.codility.com/programmers/lessons/8-leader/equi_leader

from collections import namedtuple

MaxCount = namedtuple('MaxCount', ('number', 'count'))

def dominator(A):
    counts = {}
    max_count = MaxCount(None, 0)
    for number in A:
        counts[number] = counts.get(number, 0) + 1
        if counts[number] > max_count.count:
            max_count = MaxCount(number, counts[number])

    result = max_count if max_count.count > len(A)/2 else MaxCount(None, 0)
    return result

def solution(A):
    leader, r_count = dominator(A)
    if leader is None:
        return 0

    r_len = len(A)
    l_count = 0
    l_len = 0
    equi_leader_count = 0

    for number in A:
        l_len += 1
        r_len -= 1
        if number == leader:
            r_count -= 1
            l_count += 1
        if l_count*2 > l_len and r_count*2 > r_len:
            equi_leader_count += 1

    return equi_leader_count
