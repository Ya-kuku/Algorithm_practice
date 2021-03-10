def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                stack.pop()
    else:
        if stack:
            return False
    return True
print(solution(")()("))
