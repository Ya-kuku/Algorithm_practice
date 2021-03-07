def solution(skill, skill_trees):
    answer = 0
    for tech in skill_trees:
        skill = list(skill)
        stack = []
        for i in range(len(skill)):
            for j in range(len(tech)):
                if skill[i] == tech[j]:
                    stack.append((tech[j],j))
        stack.sort(key=lambda x:x[1])
        if stack:
            tmp_skill = list(skill)
            for k in range(len(stack)):
                if stack[k][0] != tmp_skill[0]:
                    break
                elif stack[k][0] != tmp_skill[0] and stack[k][1] > stack[k+1][1]:
                        break
                else:
                    tmp_skill.pop(0)
            else:
                answer += 1
        else:
            answer += 1
    return answer

a = "CBD"
b = ["C", "D", "CB", "BDA"]
print(solution(a,b))


def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer