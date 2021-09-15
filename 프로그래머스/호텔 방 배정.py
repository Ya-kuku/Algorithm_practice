import sys
sys.setrecursionlimit(10**6)
def findEmptyRoom(number, rooms):  # 빈방을 찾는 함수
    if number not in rooms:
        rooms[number] = number + 1
        return number

    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = dict()  # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)

    return answer

solution(10,[1,3,4,1,3,1])


# def solution(k, room_number):
#     room_dic = {}
#     ret = []
#     for i in room_number:
#         n = i
#         visit = [n]
#         while n in room_dic:
#             n = room_dic[n]
#             visit.append(n)
#         ret.append(n)
#         for j in visit:
#             room_dic[j] = n+1
#     return ret