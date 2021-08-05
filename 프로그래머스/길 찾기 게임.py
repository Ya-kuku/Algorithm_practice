import sys
sys.setrecursionlimit(10 ** 6)

preorder = []
postorder = []

def solution(nodeinfo):
    n = nodeinfo[:]
    n.sort(key=lambda data : (-data[1],data[0]))

    nodes = []
    for x in n:
        nodes.append((nodeinfo.index(x)+1,x))

    levels = sorted(list(set(x[1] for x in nodeinfo)), reverse=True)
    order(nodes,levels,0)

    return [preorder, postorder]

def order(nodes,levels,cur_level):

    node = nodes[:]
    cur = node.pop(0)
    preorder.append(cur[0])

    if node:
        for i in range(len(node)):
            if node[i][1][1] == levels[cur_level + 1]:
                if node[i][1][0] < cur[1][0]:
                    order([x for x in node if x[1][0] < cur[1][0]], levels, cur_level + 1)
                else:
                    order([x for x in node if x[1][0] > cur[1][0]], levels, cur_level + 1)

    postorder.append(cur[0])

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
print(preorder)
print(postorder)