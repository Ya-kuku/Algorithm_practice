date = [31,29,31,30,31,30,31,31,30,31,30]

for tc in range(int(input())):
    m , d = map(int,input().split())
    print('#{} {}'.format(tc+1,(sum(date[:m-1]) + d + 3) % 7))
