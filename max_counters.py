# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N, A):
    max_counter = N + 1
    max_value = 0
    result = [0,]*N
    #remove consecutive duplicates of max_counter
    operations = [v for i, v in enumerate(A) if i == 0 or v != A[i-1] or v!=max_counter]

    for operation in operations:
        if operation == max_counter:
            result = [max_value,]*N
        else:
            result[operation-1]=result[operation-1]+1
            if result[operation-1]>max_value:
                max_value=result[operation-1]

    return result
