N = int(input())
hills = []
for i in range(N):
    hills.append(int(input()))
hills.sort()
costs = 1e9
for i in range(0, 83):
    tempcost = 0

    for hill in hills: 
        if hill < i:
            tempcost += ((i - hill) * (i - hill))
        elif hill > i + 17:
            tempcost += ((hill - (i + 17)) * (hill - (i + 17)))

    costs = min(costs, tempcost)
print(costs)