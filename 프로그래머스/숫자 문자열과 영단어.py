nums = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
def solution(s):
    answer = ''
    stack = ''
    for i in range(len(s)):
        if s[i].isalpha():
            stack += s[i]
            if stack in nums:
                answer += str(nums[stack])
                stack = ''
        else:
            answer += str(s[i])
    return int(answer)

print(solution("one4seveneight"))