# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish
from collections import namedtuple

Fish = namedtuple("Fish", ('size', 'direct'))

def solution(A, B):
    fish_stack = [Fish(A.pop(0), B.pop(0))]
    for size, direct in zip(A, B):
        fish = Fish(size, direct)
        
        while fish_stack and not fish.direct and fish_stack[-1].direct:
            if fish.size > fish_stack[-1].size:
                fish_stack.pop() # fish eats from stack
            else:
                break # fish is eaten
        else:
            fish_stack.append(fish) # fish survived for now
    
    return len(fish_stack)
