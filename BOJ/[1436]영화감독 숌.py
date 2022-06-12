import sys

n = int(sys.stdin.readline())
num = 666

def is_doom(num):
    while num > 0:
        if num % 1000 == 666:
            return True
        num //= 10
    return False

cnt = 0
while True:
    if is_doom(num):
        cnt += 1
        if cnt == n:
            break
    num += 1

print(num)