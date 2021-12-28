# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    number_as_str = format(N, 'b')
    number_as_str = number_as_str.strip('0')
    gaps = number_as_str.split('1')
    longest_gap = max([len(gap) for gap in gaps])
    return longest_gap
