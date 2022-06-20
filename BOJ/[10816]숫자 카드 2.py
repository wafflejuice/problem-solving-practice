import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
target_cards = list(map(int, sys.stdin.readline().rstrip().split()))

cnts_dict = dict()
for card in cards:
    if card not in cnts_dict:
        cnts_dict[card] = 0
    cnts_dict[card] += 1
    
target_cnts = [0 for _ in range(m)]
for i, target_card in enumerate(target_cards):
    if target_card in cnts_dict:
        target_cnts[i] = cnts_dict[target_card]

print(' '.join(list(map(str, target_cnts))))