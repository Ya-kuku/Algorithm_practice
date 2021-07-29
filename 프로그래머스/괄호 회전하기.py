def solution(s):
    answer = 0
    st = 0
    while st < len(s):
        stack = []
        if s[0] in '],},)':
            st += 1
            s = s[1:] + s[0]
            continue
        else:
            for i in range(len(s)):
                if not stack:
                    stack.append(s[i])
                else:
                    if stack[-1] == '[' and s[i] == ']':
                        stack.pop()
                    elif stack[-1] == '{' and s[i] == '}':
                        stack.pop()
                    elif stack[-1] == '(' and s[i] == ')':
                        stack.pop()
                    else:
                        if s[i] in '],},)':
                            break
                        stack.append(s[i])
            if not stack:
                answer += 1

        st += 1
        s = s[1:] + s[0]
    print(answer)
    return answer

solution('[](){}')