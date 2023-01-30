def solution(number):
    answer = 0
    n = len(number)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                print(number[i],number[j],number[k])
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    print(answer)
    return answer

solution([-3, -2, -1, 0, 1, 2, 3])