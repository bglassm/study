def solution(k, m, score):
    answer=0
    sorted_score=sorted(score)
    w_sales=sorted_score[len(score)%m:]
    for i in range(0, len(w_sales), m):
        answer += w_sales[i] * m
    return answer