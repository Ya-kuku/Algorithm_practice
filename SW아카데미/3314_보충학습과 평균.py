for T in range(int(input())):
    score = list(map(int,input().split()))
    average = 0
    for i in range(len(score)):
        if score[i] < 40:
            average += 40
        else:
            average += score[i]
    print('#{} {}'.format(T+1,average // len(score)))