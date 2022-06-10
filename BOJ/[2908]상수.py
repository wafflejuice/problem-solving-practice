import sys

print(max(map(lambda x:int(''.join(list(reversed(x)))), sys.stdin.readline().rstrip().split())))