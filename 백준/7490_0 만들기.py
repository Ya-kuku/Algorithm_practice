import copy
def solve(array, n):
    if len(array) == n:
        operators.append(copy.deepcopy(array))
        return

    array.append(' ')
    solve(array,n)
    array.pop()

    array.append('+')
    solve(array, n)
    array.pop()

    array.append('-')
    solve(array, n)
    array.pop()

for tc in range(int(input())):
    N = int(input())
    operators = []
    print(operators)
    # N 범위에 따라 들어갈 수 있는 연산자 위치는 N-1개
    solve([],N-1)

    calculate = [i for i in range(1,N+1)]

    for operator1 in operators:
        num = ''
        # 연산자 위치
        for i in range(N-1):
            num += str(calculate[i]) + operator1[i]
        num += str(calculate[-1])
        if eval(num.replace(' ','')) == 0:
            print(num)
    print()