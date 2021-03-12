# 시간초과
# def solution(record):
#     answer = []
#     record = [ i.split() for i in record]
#     temp = []
#     # 0 들어옴, 1 나감
#     for i in record:
#         if i[0] == 'Enter':
#             # 아이디, 출/입, uid
#             temp.append([i[2],0,i[1]])
#             for k in temp:
#                 if i[1] == k[2]:
#                     k[0] = i[2]
#         elif i[0] == 'Leave':
#             for k in temp:
#                 if i[1] == k[2]:
#                     temp.append([k[0],1,i[1]])
#                     break
#         else:
#             # 실행문 저장된 리스트
#             for j in temp:
#                 # 실행문에 저장된 아이디 바꿔주기
#                 # uid 비교
#                 if j[2] == i[1]:
#                     j[0] = i[2]
#     for res in temp:
#         if not res[1]:
#             answer.append(res[0] + '님이 들어왔습니다.')
#         else:
#             answer.append(res[0] + '님이 나갔습니다.')
#     return answer

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# solution(record)

# 딕션 방법1
# def solution(record):
#     answer = []
#     infor = {}
#     for r in record:
#         r = r.split()
#         # unpack
#         if len(r) == 3:
#             code, uid, name = r
#         else:
#             code, uid = r
#
#         if code == 'Enter':
#             if uid not in infor:
#                 # 처음 들어왔으면
#                 answer.append("{}님이 들어왔습니다.".format(name))
#                 infor[uid] = [name, [len(answer) - 1]]
#             else:
#                 # 이름을 바꾸고 들어왔으면
#                 if name != infor[uid][0]:
#                     # 갱신을 위해 이전 이름 길이 저장
#                     t_l = len(infor[uid][0])
#                     # answer에 있는 이름 갱신
#                     for idx in infor[uid][1]:
#                         answer[idx] = name + answer[idx][t_l:]
#                     infor[uid][0] = name
#                     answer.append("{}님이 들어왔습니다.".format(name))
#                     infor[uid][1].append(len(answer) - 1)
#                 # 그냥 다시 들어온거라면
#                 else:
#                     answer.append("{}님이 들어왔습니다.".format(name))
#                     infor[uid][1].append(len(answer) - 1)
#         elif code == 'Leave':
#             answer.append("{}님이 나갔습니다.".format(infor[uid][0]))
#             infor[uid][1].append(len(answer)-1)
#
#         elif code == 'Change':
#             t_l = len(infor[uid][0])
#             infor[uid][0] = name
#             for idx in infor[uid][1]:
#                 answer[idx] = name + answer[idx][t_l:]
#     return answer
#
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# solution(record)

# 딕션 방법2
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)