import sys

t = int(sys.stdin.readline())
for _ in range(t):
    results = sys.stdin.readline().rstrip()
    score = 0
    combo = 0
    for result in results:
        if result == 'O':
            combo += 1
        else:
            combo = 0
        score += combo
    print(score)