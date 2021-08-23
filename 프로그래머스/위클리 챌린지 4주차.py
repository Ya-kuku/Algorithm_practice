def solution(table, languages, preference):
    answer = ''
    tables = {}
    ans = []
    for ta in table:
        ta = ta.split()
        tables[ta[0]] = {}
        for a in range(1,6):
            tables[ta[0]][ta[a]] = 6-a

    print(tables)
    for i in ['SI','CONTENTS','HARDWARE','PORTAL','GAME']:
        cnt = 0
        for j in range(len(languages)):
            if languages[j] in tables[i]:
                cnt += tables[i][languages[j]] * preference[j]
        ans.append([i,cnt])
    ans.sort(reverse= True, key=lambda data:(-data[1],data[0]))
    print(ans)
    return ans[-1][0]

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
         ,["JAVA", "JAVASCRIPT"],[7, 5])