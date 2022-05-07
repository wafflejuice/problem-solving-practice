input_split = input().split()
n = int(input_split[0])
m = int(input_split[1])

listen = set()
both = set()

for ni in range(n):
    listen.add(input())
for mi in range(m):
    se = input()
    if se in listen:
        both.add(se)
        listen.remove(se)

both = sorted(both)
cnt = len(both)
print(cnt)
for e in both:
    print(e)