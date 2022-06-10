import sys

notes = list(map(int, sys.stdin.readline().rstrip().split()))
if notes == sorted(notes):
    print('ascending')
elif notes == sorted(notes, reverse=True):
    print('descending')
else:
    print('mixed')