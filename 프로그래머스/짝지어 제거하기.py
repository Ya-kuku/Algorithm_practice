def solution(s):
    if len(s) % 2:
        return 0
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        elif stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1


solution('baabaa')