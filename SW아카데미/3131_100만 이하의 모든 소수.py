seive = [False, False] + [True] * (1000000 - 1)
for k in range(2, int(1000000 ** 0.5 + 1.5)):
    if seive[k]:
        seive[k*2::k] = [False] * ((1000000 - k) // k)
for i in range(len(seive)):
    if seive[i]:
        print(i,end=' ')