from itertools import combinations
def getPrimeList(n):
    seive = [False,False] + [True] * n

    for i in range(2,int(n**0.5)+1):
        if seive[i]:
            # 처음 소수의 다음 배수 부터 범위 지정
            for j in range(2*i,n,i):
                seive[j] = False

    # return [i for i in range(2,n) if seive[i]]
    return seive
def solution(nums):
    answer = 0

    pos_nums = list(combinations(nums,3))

    num = []
    for pos in pos_nums:
        num.append(sum(pos))

    seive = getPrimeList(3000)


    for i in num:
        if seive[i]:
            answer += 1
    return answer