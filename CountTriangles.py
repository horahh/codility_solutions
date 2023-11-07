# https://app.codility.com/demo/results/trainingNKJE84-UGH/

def solution(A):
    # Implement your solution here
    if len(A)< 3:
        return 0
    A.sort()

    
    count=0
    for i in range(0,len(A)-2):
        j,k=i+1,i+2
        while j<len(A)-1:
            if k < len(A) and A[i]+A[j] > A[k]:
                count += k-j
                k+=1
            else:
                j+=1
    return count
