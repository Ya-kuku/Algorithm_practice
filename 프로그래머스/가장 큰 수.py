def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

a = [[6,10,2],[3,30,34,5,9]]
for i in a:
    solution(i)