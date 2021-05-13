from itertools import permutations
N, K = map(int,input().split())
kits = list(map(int,input().split()))
pos_kits = list(permutations(kits,N))
ans = len(pos_kits)

for kit in pos_kits:
    days = 0
    weight = 500
    while days < N:
        weight -= K
        weight += kit[days]
        if weight < 500:
            ans -= 1
            break
        else:
            days += 1
print(ans)