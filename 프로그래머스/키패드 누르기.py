phone = {
    1:(0,0),2:(0,1),3:(0,2),
    4:(1,0),5:(1,1),6:(1,2),
    7:(2,0),8:(2,1),9:(2,2),
    '*':(3,0),0:(3,1),'#':(3,2)
         }

def solution(numbers, hand):
    answer = ''
    left_hand = '*'
    right_hand = '#'
    for num in numbers:
        if num in [1,4,7]:
            left_hand = num
            answer += 'L'
        elif num in [3,6,9]:
            right_hand = num
            answer += 'R'
        else:
            x,y = phone[num]
            left_dist = abs(phone[left_hand][0]- x) + abs(phone[left_hand][1]-y)
            right_dist = abs(phone[right_hand][0]- x) + abs(phone[right_hand][1]-y)

            if left_dist < right_dist:
                left_hand = num
                answer += 'L'
            elif right_dist < left_dist:
                right_hand = num
                answer += 'R'
            else:
                if hand == 'right':
                    right_hand = num
                    answer += 'R'
                else:
                    left_hand = num
                    answer += 'L'
    print(answer)
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")