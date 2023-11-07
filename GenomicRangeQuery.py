
# https://app.codility.com/demo/results/trainingQAHVQG-CAS/

letters='ACGT'

def solution(S, P, Q):
    # Implement your solution here    
    letters_acc = { letter:0 for letter in letters }
    S_prefix_sum = [ prefix_sum(s,letters_acc) for s in S ]
    result = [ get_range_min(p,q,S_prefix_sum,S) for p,q in zip(P,Q) ]
    return result

def prefix_sum(s,letters_acc):
    letters_acc[s]+=1
    return letters_acc.copy()

def get_range_min(p,q,S_pre,S):
    letter_to_value = { letter:value+1 for value,letter in enumerate(letters)}
    if q < p:
        p,q = q,p
    for letter in letters:
        letter_count = S_pre[q][letter]-S_pre[p][letter]
        if S[p] == letter:
            letter_count = letter_count +1
        if letter_count > 0:
            return letter_to_value[letter]
    return None
