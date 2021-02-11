#중위 순회는 x축을 기준으로 왼쪽부터 방문한다
class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node,level):
    global level_depth, x
    level_depth = max(level_depth,level)

    if node.left_node != -1:
        # 자식 노드가 있는 경우니까 깊이 +1
        in_order(tree[node.left_node], level + 1)
    # 해당 레벨에 가장 작은값과 큰값을 저장해서 나중에 너비를 구하기 위해 사용
    # 재귀적으로 생각하면 맨 밑 왼쪽 노드까지 재귀적으로 들어가고, 제일 깊은 레벨의 값이 1로 시작됨

    # 이 부분이 헷갈리니까 디버깅 돌려보자
    # x값은 중위순회니까 왼쪽부터 차례대로 한칸씩 숫자 올라간다고 생각하면 됨
    print(x)
    # 재귀적으로 탐색하면 예를들어 3번깊이에서 1번째라는 값을 저장했을 때, 해당레벨에서 최소값과 최대값을 저장해두고
    # 기본적으로 최소값은 거의 계속 고정이 될것이고, 최대값은 깊이마다 채워진 x의 값이 늘어나기 때문에 기존값보다 큰값들이 계속 변경되면서 저장됨
    level_min[level] = min(level_min[level], x)
    print(level_min)
    level_max[level] = max(level_max[level], x)
    print(level_max)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)
n = int(input())
tree = dict()
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1,n+1):
    # left와 right를 비어있다고 가정하고 -1로 초기화
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    number, left_node, right_node = map(int,input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    # 왼쪽/오른쪽 노드가 들어있다면, 그 노드의 부모 노드는 number로 저장
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

for i in range(1, n+1):
    # 전체 트리 중 해당 노드의 부모노드 값이 -1이면, 루트노드가 된다
    if tree[i].parent == -1:
        root = i

# 처음 시작 레벨은 1
in_order(tree[root],1)

result_level = 1
# 너비의 초기값 지정
result_width = level_max[1] - level_min[1] + 1
for i in range(2,level_depth+1):
    width = level_max[i] - level_min[i] + 1
    # 각 레벨의 너비와 깊이 비교
    if result_width < width:
        result_level = i
        result_width = width

print(result_level,result_width)
