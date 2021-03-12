def solution(n, words):
    answer = [0,0]
    print(words)
    stack = [words[0]]
    for i in range(1,len(words)):
        if words[i] not in stack and words[i][0] == stack[-1][-1]:
            stack.append(words[i])
        else:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
    print(answer)
    return answer
solution(2,["hello", "one", "even", "never", "now", "world", "draw"])