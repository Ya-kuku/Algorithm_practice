for tc in range(int(input())):
    N, A, B = map(int,input().split())
    Max = min(A,B)
    if A + B <= N:
        Min = 0
    else:
        Min = A+B-N
    print('#{} {} {}'.format(tc+1,Max,Min))