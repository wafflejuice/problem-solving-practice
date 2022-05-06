input_split = input().split()
n = int(input_split[0])
r = int(input_split[1])
c = int(input_split[2])

div = 2**(n-1)
idx = 0
while div > 0:
    idx += (2 * (r // div) + (c // div)) * div * div
    
    r %= div
    c %= div
    div //= 2

print(idx)
