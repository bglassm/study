def solution(n):
    k=n
    b3_n=[]
    answer=0
    while k:
        b3_n.append(k%3)
        k=k//3

    for i,j in enumerate(b3_n):
        answer+=j*(3**(len(b3_n)-i-1))
        print(i,j)
    return answer