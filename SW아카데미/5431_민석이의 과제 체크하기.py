for tc in range(int(input())):
    N, K = map(int,input().split())
    report = [0] * 101
    student = list(map(int,input().split()))
    for i in range(K):
        report[student[i]] = 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(1,N+1):
        if report[i] == 0:
            print(i,end=' ')
    print()