
# https://app.codility.com/demo/results/training9K822K-SSZ/
def solution(A):
    # Implement your solution here
    S = { abs(a) for a in A}
    return len(S)
