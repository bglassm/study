def solution(food):
    flist = [int(i) for i in food]

    for i in range(1, len(flist)):
        if flist[i] % 2 != 0:
            flist[i] = int((flist[i] - 1)/2)
        else:
            flist[i] = int(flist[i]/2)
    hresult = [str(i) * flist[i] for i in range(len(flist))]
    hresult.pop(0)
    hrestr = ''.join(hresult)
    hresult.reverse()
    rhrestr =''.join(hresult)
    answer=hrestr+"0"+rhrestr    

    return answer
