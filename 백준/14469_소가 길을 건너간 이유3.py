n = int(input())
cow = []
for _ in range(n):
    cow.append(list(map(int,input().split())))
cow.sort()
time = 0
for co in cow:
    if co[0] > time:
        time = sum(co)
    else:
        time += co[-1]
print(time)