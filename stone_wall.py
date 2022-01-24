# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall

def solution(H):
    blocks = []
    active_blocks = [H.pop(0)]
    for h in H:
        if h > active_blocks[-1]:
            # must create new active block
            active_blocks.append(h)
        while active_blocks and h <= active_blocks[-1]:
            if h == active_blocks[-1]:
                # found 'reusable' block
                break
            # block can't be reused anymore, smaller block will be appended
            blocks.append(active_blocks.pop())
        else:
            # 'reusable' block not found, appending new
            active_blocks.append(h)

    return len(blocks) + len(active_blocks)
