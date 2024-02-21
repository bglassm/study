def solution(N, stages):
    sn=[]
    fr=[]
    pn_now=len(stages)
    for i in range (1,N+1):
        sn.append(stages.count(i))
    sn.append(stages.count(N+1))
    print(sn)
    for i in range (0,N):
        fr.append(sn[i]/pn_now)
        pn_now=pn_now-sn[i]
    tuple_fr=[(value, index) for index, value in enumerate(fr)]
    sorted_fr=sorted(tuple_fr, key=lambda x: (-x[0], x[1]))
    answer=[1+index for value, index in sorted_fr]

    return answer 