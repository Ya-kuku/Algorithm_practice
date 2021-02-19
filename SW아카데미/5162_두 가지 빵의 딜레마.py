for tc in range(int(input())):
    A,B,C = map(int,input().split())
    print('#{} {}'.format(tc+1,C // min(A,B)))