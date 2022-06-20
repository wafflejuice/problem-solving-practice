import sys

n = int(sys.stdin.readline())

i = 0
while True:
    if n <= 1 + 6 * i * (i + 1) // 2:
        print(1+i)
        break
    i += 1