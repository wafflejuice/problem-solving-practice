import sys

t = int(sys.stdin.readline())
for ti in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    integers = sys.stdin.readline().rstrip()[1:-1].split(',')

    i, j = -1, n
    is_front = True
    for func in p:
        if func == "R":
            is_front = not is_front
        else:
            if i + 1 == j:
                print('error')
                break
            if is_front:
                i += 1
            else:
                j -= 1
    else:
        if is_front:
            print('[' + ','.join(integers[i + 1:j]) + ']')
        else:
            print('[' + ','.join(reversed(integers[i + 1:j])) + ']')