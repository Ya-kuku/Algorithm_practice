def solution(sizes):
    answer = 0
    Max = 0
    Min = 0
    for size in sizes:
        Max = max(max(size),Max)
        Min = max(min(size),Min)
    return Max * Min