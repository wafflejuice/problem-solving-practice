import sys
import heapq

n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split()))
coords_q = coords.copy()
coord_to = dict()

heapq.heapify(coords_q)
i = 0
precoord = ''
while len(coords_q) > 0:
    coord = heapq.heappop(coords_q)

    if precoord == coord:
        continue
    precoord = coord

    coord_to[coord] = str(i)
    i += 1

for pi in range(len(coords)):
    coords[pi] = coord_to[coords[pi]]

print(' '.join(coords))
