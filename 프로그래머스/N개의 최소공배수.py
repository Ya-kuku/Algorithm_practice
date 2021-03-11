def gcd(a,b):
    while b !=0:
        d = a % b
        a = b
        b = d
    return a

def solution(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        arr[i+1] = arr[i]*arr[i+1] // gcd(arr[i],arr[i+1])
    return arr[-1]