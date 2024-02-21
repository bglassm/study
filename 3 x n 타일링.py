def solution(n):
    bn=int(n/2)
    nc_list=[0]*(bn+1)
    nc_list[0]=1
    nc_list[1]=3
    sum_pre=0
    for i in range(2,bn+1):
        sum_pre += nc_list[i-2]
        nc_list[i] = (3 * nc_list[i-1] + 2 * sum_pre)
    answer=nc_list[bn]%1000000007
    return answer