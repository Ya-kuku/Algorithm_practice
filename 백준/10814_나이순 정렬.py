N = int(input())
ans = []
for _ in range(N):
    age, name = map(str,input().split())
    ans.append((int(age),name))
ans.sort(key=lambda x:x[0])
for i in range(N):
    print(ans[i][0],ans[i][1])