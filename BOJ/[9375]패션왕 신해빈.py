import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline())
	clothes = dict()
	for _ in range(n):
		cloth, group = sys.stdin.readline().rstrip().split()
		if group not in clothes:
			clothes[group] = 0
		clothes[group] += 1
	
	product = 1
	for cnt in clothes.values():
		product *= (cnt + 1)
	print(product-1)

