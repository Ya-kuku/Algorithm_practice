for tc in range(int(input())):
    N = int(input())
    avg = 0
    for _ in range(N):
        a,b = map(float,input().split())
        avg += a * b
    print(avg)
    print('#%d %f' %(tc+1,avg))