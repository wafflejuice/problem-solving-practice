def solution(absolutes, signs):
    sum_=0
    for absolute, sign in zip(absolutes, signs):
        sum_ += absolute if sign else -absolute
    return sum_