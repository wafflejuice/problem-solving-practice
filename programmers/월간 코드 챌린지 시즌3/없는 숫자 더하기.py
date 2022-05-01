def solution(numbers):
    return sum(list(filter(lambda x:x not in numbers, [i for i in range(10)])))