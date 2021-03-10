# def solution(citations):
#     return max([min(i+1,sorted(citations, reverse=True)[i]) for i in range(len(citations))])

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

solution([3,0,6,1,5])