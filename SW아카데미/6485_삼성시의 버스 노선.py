for tc in range(int(input())):
    station = [0] * 5001
    N = int(input())
    bus = [tuple(map(int,input().split())) for _ in range(N)]
    P = int(input())
    st_no = [int(input()) for _ in range(P)]
    for i in bus:
        for j in range(i[0],i[1]+1):
            station[j] += 1
    print('#{}'.format(tc+1),end=' ')
    for i in st_no:
        print(station[i],end='')



