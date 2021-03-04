# import queue
# a = queue.PriorityQueue()
# a.put(1)
# a.put(11)
# a.put(7)
# a.put(2)
#
# while a:
#     print(a.get())

def solution(priorities, location):
    answer = 0
    tmp = []
    for i in range(len(priorities)):
        tmp.append((priorities[i],i))
    stack = []
    while tmp:
        a = tmp.pop(0)
        for i in tmp:
            if a[0] < i[0]:
                tmp.append(a)
                break
        else:
            stack.append(a)
    print(tmp)
    for i in stack:
        if i[1] == location:
            answer = stack.index(i)
            break
    return answer