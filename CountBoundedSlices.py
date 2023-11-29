
# pending to figure out what is wrong with this approach, having 60% failing some random sequences
# https://app.codility.com/demo/results/trainingE47D45-GKB/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

MAXIMUM = 1_000_000_000

def solution(K, A):
    # Implement your solution here

    max_q=deque()
    min_q=deque()
    count=0
    maximum=A[0]
    minimum=A[0]
    range_start=0
    min_clear_index=0
    max_clear_index=0

    for i,a in enumerate(A):
        if max_q and max_q[0]<a:
            max_q.clear()
            max_clear_index=i        
        max_q.append(a)
        if min_q and min_q[0]>a:
            min_q.clear()
            min_clear_index=i
        min_q.append(a)

        while range_start < i and max_q[0]-min_q[0] > K :
            range_start+=1
            if max_clear_index < range_start:
                max_q.popleft()
                max_clear_index+=1
            if min_clear_index < range_start:
                min_q.popleft()
                min_clear_index+=1       
       
        delta=i-range_start+1
        count+=delta
        #print(f"{min_q[0]=} {max_q[0]=} {delta=} {count=}")
        if count >=MAXIMUM:
            return MAXIMUM

    return count
