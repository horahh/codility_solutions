# https://app.codility.com/demo/results/trainingDEWR4H-TBJ/

import math
def solution(N):
    if N==1:
        return 1
    # Implement your solution here
    n_sqrt= math.ceil(math.sqrt(N))
    factors = 2
    for i in range(2,n_sqrt):
        if N % i:
            continue
        factors +=2
    if n_sqrt*n_sqrt==N:
        factors+=1
    return factors
