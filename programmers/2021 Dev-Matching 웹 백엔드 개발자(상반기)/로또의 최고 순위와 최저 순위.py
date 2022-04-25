def solution(lottos, win_nums):
    unknown_cnt=lottos.count(0)
    correct_cnt=len(list(filter(lambda num:num in win_nums, lottos)))

    min_correct_cnt=correct_cnt
    max_correct_cnt=correct_cnt+unknown_cnt

    return [min(6, 7-max_correct_cnt), min(6, 7-min_correct_cnt)]