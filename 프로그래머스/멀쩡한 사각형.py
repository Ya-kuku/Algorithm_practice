# gcd(greatest common divisor 최대 공약수) 반복문
def gcd(a,b):
    while b !=0:
        d = a % b
        a = b
        b = d
    return a
def solution(w,h):
    answer = w * h
    tmp = gcd(w,h)
    return answer - (w + h- tmp)

# gcd 재귀적방법
# def gcd(m,n):
#     if m < n:
#         m,n = n,m
#     if n == 0:
#         return m
#     if m % n == 0:
#         return n
#     else:
#         return gcd(n,m%n)

# lcm(최소 공배수)
# 두 숫자의 곱에 최대공약수를 나눠준 값이 최소 공배수가 된다
# def lcm(a, b):
#     return a*b//gcd(a,b)