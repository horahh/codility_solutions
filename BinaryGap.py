
#  https://app.codility.com/demo/results/training67Y6QU-TS8/

def solution(N):
    # Implement your solution here
    count_gap = 0
    #need to count the gap when is valid, there is a 1 at the left, step when finding 1 at right
    count_gap_valid = False
    max_gap=0
    while N:
        lsb=N&1
        if lsb:
            count_gap_valid =True
            max_gap = max(max_gap,count_gap)
            count_gap=0
        elif count_gap_valid:
            count_gap+=1
        N >>= 1


    return max_gap
