NOTATION = '0123456789ABCDEF'

def convert(num, base) :
    q, r = divmod(num, base)
    n = NOTATION[r]
    return convert(q, base) + n if q else n

def solution(n, t, m, p):
    # n = 진법, t = 변환시켜야할 숫자까지, m = 참가인원, p = 해당순서
    answer = ''
    res = ''
    for i in range(10**6):
        res += convert(i,n)
        if len(res) > t*m:
            break
    print(res)
    for i in range(0,len(res),m):
        answer += res[i+p-1]
        if len(answer) == t:
            break
    return answer

print(solution(2,4,2,1))


