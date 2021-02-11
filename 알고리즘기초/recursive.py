def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
print(factorial(10))

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        # string 1:-1 부분을 재귀 호출
        return palindrome(string[1:-1])
    else:
        return False

def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2:
        return func((3 * n) + 1)
    else:
        return (func(int(n / 2)))

# print(func(3))


# 정수 n을 1,2,3의 조합으로 나타내는 경우

def func2(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    else:
        return func2(data-1) + func2(data-2) + func2(data-3)

print(func2(5))


