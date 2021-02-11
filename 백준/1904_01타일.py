N = int(input())
array = [0] * 10000001
array[1] = 1
array[2] = 2
for i in range(3,N+1):
    array[i] = (array[i-2] + array[i-1]) % 15746

print(array[N])
