def solution(answers):
    scores = [0, 0, 0]
    picks = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
             [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for ai, answer in enumerate(answers):
        for i in range(3):
            if answer == picks[i][ai % len(picks[i])]:
                scores[i] += 1

    candidates = []
    for i in range(3):
        if scores[i] == max(scores):
            candidates.append(i+1)

    return sorted(candidates)