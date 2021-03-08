def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 1:
            answer += '1'
        elif n % 3 == 2:
            answer += '2'
        else:
            answer += '4'
        n = n // 3
    return answer[::-1]