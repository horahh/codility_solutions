
# https://app.codility.com/demo/results/training4H7Q5C-J44/

def solution(A):
    # Implement your solution here
    k=0
    count=1
    while A[k]!= -1:
        count+=1
        k=A[k]
    return count
