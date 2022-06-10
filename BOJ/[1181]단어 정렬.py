import heapq
import sys

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    heapq.heappush(words, (len(word), word))

pre = None
while len(words) > 0:
    _, word = heapq.heappop(words)
    if word != pre:
        print(word)
        pre = word
