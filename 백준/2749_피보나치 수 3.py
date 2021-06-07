N = int(input())

# 피사노 주기 사용
# 나누는 숫자가 10 ** n 이면 주기는 15 * (10**(n-1))
mod = 1000000
fibo = [0,1]
p = (mod // 10) * 15

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= mod

print(fibo[N%p])