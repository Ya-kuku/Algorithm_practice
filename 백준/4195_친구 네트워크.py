# def check():
#     for i in tmp:
#         if i[0] in network or i[1] in network:
#             network.add(i[0])
#             network.add(i[1])
#     return len(network)
#
# for tc in range(int(input())):
#     F = int(input())
#     network = set()
#     A, B = map(str,input().split())
#     network.add(A)
#     network.add(B)
#     print(len(network))
#     tmp = set()
#     for _ in range(F-1):
#         X,Y = map(str,input().split())
#         if X in network or Y in network:
#             network.add(X)
#             network.add(Y)
#         else:
#             tmp.add((X,Y))
#         print(check())
#

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        # 이전 네트워크의 크기를 더해준다
        number[x] += number[y]

for tc in range(int(input())):
    parent = dict()
    number = dict()

    # 친구 관계 수
    F = int(input())

    for _ in range(F):
        X, Y = input().split()

        # 해당 값이 네트워크에 존재하지 않으면 네트워크에 포함시켜준다
        if X not in parent:
            parent[X] = X
            number[X] = 1
        if Y not in parent:
            parent[Y] = Y
            number[Y] = 1

        union(X,Y)
        print(number[find(X)])
