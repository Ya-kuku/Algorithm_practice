def fibo(n):
    for i in range(2,n+1):
        ans[i] = ans[i-1] +ans[i-2]
    return ans[n]
ans = [0] * 46
ans[1] = 1
ans[2] = 1
n = int(input())
print(fibo(n))