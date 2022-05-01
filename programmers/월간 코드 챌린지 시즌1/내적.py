def solution(a, b):
    sum_ = 0
    for i, j in zip(a, b):
        sum_ += i*j
    return sum_