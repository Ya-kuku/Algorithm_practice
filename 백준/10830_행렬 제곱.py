def mul(n,lst1,lst2):
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += lst1[i][k] * lst2[k][j]
            if res[i][j] >= 1000:
                res[i][j] %= 1000

    return res

def devide(n,b,lst):
    if b == 1:
        return lst
    elif b == 2:
        return mul(n,lst,lst)

    # 거듭제곱이 2보다 큰 경우
    else:
        tmp = devide(n,b//2,lst)
        if b % 2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),lst)

N, B = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
res = devide(N,B,arr)

for r in res:
    for n in r:
        print(n%1000,end=' ')
    print()

