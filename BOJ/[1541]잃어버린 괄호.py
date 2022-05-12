import sys

line=sys.stdin.readline()

formula = []
signs = []
start = 0
for i, ch in enumerate(line):
    if ch == '+' or ch == '-':
        formula.append(int(line[start:i]))
        signs.append(ch)
        start = i+1
formula.append(int(line[start:]))

i = 0
while i < len(signs):
    if signs[i] == '+':
        signs.pop(i)
        formula[i] += formula[i+1]
        formula.pop(i+1)
    else:
        i += 2
        
ans = formula[0]
for i in range(1, len(formula)):
    ans -= formula[i]

print(ans)