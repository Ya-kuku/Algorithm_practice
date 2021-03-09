from itertools import permutations
def check(n,nums):
    seive = [False,False] + [True] * (n - 2)

    for i in range(2, int(n ** 0.5) + 1):
        if seive[i]:
            # 처음 소수의 다음 배수 부터 범위 지정
            for j in range(2 * i, n, i):
                seive[j] = False

    cnt = 0
    for num in nums:
        if seive[num]:
            cnt += 1
    return cnt

def solution(numbers):
    temp = []
    for i in range(1,len(numbers)+1):
        temp += list(permutations(numbers,i))
    nums = list(set(map(int,list([''.join(num) for num in temp]))))
    print(nums)
    answer = check(max(nums)+1,nums)
    return answer

a ='011'
print(solution(a))

# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)
