for tc in range(int(input())):
    N = int(input())
    for i in range(10**6+1):
        if i**3 == N:
            print('#{} {}'.format(tc+1,i))
            break
    else:
        print('#{} {}'.format(tc+1,-1))