def solution(n, s):
    answer=[]
    k=n
    r=s
    if s/n<1:
        answer=[-1]
    else:
        for i in range (n):
            if r/k==int(r/k):
                answer.append(int(r/k))
            else:
                answer.append(int(r/k))
                r=r-int(r/k)
                k=k-1
    return answer