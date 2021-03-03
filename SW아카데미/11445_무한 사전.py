for tc in range(int(input())):
    a = input().strip()
    b = input().strip()
    ans = 'N'
    # 사전상 순서이기 때문에 같은 경우에는 무조건 존재
    if len(a) == len(b):
        ans = 'Y'
    # a가 더 긴 경우
    elif len(a) > len(b):
        ans = 'Y'

    # b가 더 긴 경우
    else:
        if len(b) - len(a) > 1:
            ans = 'Y'
        else:
            for i in range(len(a)):
                if a[i] != b[i]:
                    ans = 'Y'
            else:
                if b[-1] != 'a':
                    ans = 'Y'

    print('#{} {}'.format(tc+1,ans))