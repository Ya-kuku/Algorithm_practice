# def rerange(data):
#     for i in range(len(data) - 1):
#         Min = i
#         for j in range(i+1,len(data)):
#             if data[Min] > data[j]:
#                 Min = j
#         # 최초의 기준점과 자리를 바꾸기 때문에 i의 값과 자리 swap
#         data[Min], data[i] = data[i], data[Min]
#     return data
#
# def solution(numbers):
#     answer = []
#     n = len(numbers)
#     for i in range(n-1):
#         current_num = numbers[i]
#         tmp_list = rerange(numbers[i:])
#         if tmp_list[-1] < current_num:
#             answer.append(-1)
#             continue
#         for j in range(i+1,n):
#             if numbers[j] > current_num:
#                 answer.append(numbers[j])
#                 break
#         else:
#             answer.append(-1)
#     answer.append(-1)
#     print(answer)
#     return answer


# def solution(numbers):
#     answer = [numbers[0]]
#     n = len(numbers)
#     for i in range(n):
#         if i != 0: answer.append(numbers[i])
#         if numbers[i] > answer[-1]:
#             answer.pop()
#             answer.append(numbers[i])
#         else:
#             answer.pop()
#             answer.append(-1)
#     print(answer)
#     return answer

def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        print(result)
        print(stack,i)
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
            print(result)
            print(stack)
        stack.append(i)

    return result

#solution([2, 3, 3, 5])
solution([9, 1, 5, 3, 6, 2])

# from heapq import heappop,heappush
#
# def solution(numbers):
#     answer = [-1 for _ in range(len(numbers))]
#     heap = [(numbers[0],0)]
#     for i,n in enumerate(numbers[1:]):
#         while heap and heap[0][0]<n:
#             _,idx = heappop(heap)
#             answer[idx] = n
#         heappush(heap,(n,i+1))
#     return answer