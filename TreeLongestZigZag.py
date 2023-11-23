# https://app.codility.com/demo/results/trainingQWPRZM-RX6/

from extratypes import Tree  # library with types used in the task

def solution(T):
    # Implement your solution here
    direction=[]    
    result=dfs(T,direction)
    if result>0:
        result-=1
    return result

def dfs(T, direction):
    left_zz=0
    right_zz=0
    l=False
    r=False
    if not T.l and not T.r:
        return len(direction)
    if T.l:
        if not direction or direction[-1]=='r':
            direction.append('l')
            l=True
        left_zz=dfs(T.l,direction)
        if l:
            direction.pop()
    if T.r:
        if not direction or direction[-1]=='l':
            direction.append('r')
            r=True
        right_zz=dfs(T.r,direction)
        if r:
            direction.pop()

    return max(left_zz,right_zz)
