# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting

def solution(S):
    stack = []
    for s in S:
        if stack and s == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)

    result = 1 if not stack else 0
    return result

