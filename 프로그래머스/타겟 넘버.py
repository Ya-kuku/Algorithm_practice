answer = 0
def dfs(idx, numbers, target, ans):
    global answer
    N = len(numbers)
    if idx == N and target == ans:
        answer += 1
        return
    if idx == N:
        return

    dfs(idx + 1, numbers, target, ans + numbers[idx])
    dfs(idx + 1, numbers, target, ans - numbers[idx])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)
#
# solution([1,1,1,1,1],3)