
# https://app.codility.com/demo/results/trainingC2YHP6-DR5/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    
    fish_downstream_stack = []
    alive =len(A)

    for a,b in zip(A,B):
        # downstream fish
        if b == 1:
            fish_downstream_stack.append(a)
            continue
        # upstream fish
        while fish_downstream_stack:
            if a < fish_downstream_stack[-1]:
                alive -=1
                break
            if a > fish_downstream_stack[-1]:
                fish_downstream_stack.pop()
                alive -=1
    return alive
