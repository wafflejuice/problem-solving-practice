import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0 and c == 0:
        break

    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print('right')
    else:
        print('wrong')