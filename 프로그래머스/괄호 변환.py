def divide(p):
    st = 0
    ed = 0

    for i in range(len(p)):
        if p[i] == '(':
            st += 1
        else:
            ed += 1
        # 처음 균형잡힌 괄호 형태 찾게되면 나누어줌
        if st == ed:
            return p[:i + 1], p[i+1:]

def isBalanced(u):
    stack = []

    for p in u:
        if p =='(':
            stack.append(p)
        else:
            # 스택이 비어있으면 즉 ')'이 처음으로 들어가야해서
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p:
        return ''

    u, v = divide(p)

    if isBalanced(u):
        # u가 올바를 괄호형이면 v에 대해서 똑같은 작업을 수행
        return u + solution(v)
    else:

        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

        return answer