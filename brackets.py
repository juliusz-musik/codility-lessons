# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets

def solution(S):
    bracket_mapping = {')':'(',
                       '}':'{',
                       ']':'['}
    
    stack = []
    for char in S:     
        if stack and bracket_mapping.get(char, None) == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    result = 1 if not stack else 0
    return result
