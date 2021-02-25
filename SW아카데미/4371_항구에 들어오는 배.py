for tc in range(int(input())):
    N = int(input())
    day = []
    for _ in range(N):
        day.append(int(input()))
    ans = 0
    for i in range(1,len(day)):
        if day[i] != 0:
            ship = day[i] - day[0]
            ans += 1
            for j in range(1,len(day)):
                if not (day[j] - 1) % ship:
                    day[j] = 0
        if sum(day) == 1:
            break
    print('#{} {}'.format(tc+1,ans))