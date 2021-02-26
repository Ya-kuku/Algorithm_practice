ans = []
for tc in range(int(input())):
    A,B,C,D = map(float,input().split())
    alice = A / B
    bob = C / D
    if alice == bob:
        res = 'DRAW'
    elif alice > bob:
        res = 'ALICE'
    else:
        res = 'BOB'
    ans.append(res)
j = 1
for i in ans:
    print('#{} {}'.format(j,i))
    j += 1