# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    filled_positions = set()
    for second, position in enumerate(A):
        filled_positions.add(position)
        if len(filled_positions) == X:
            return second
    return -1
