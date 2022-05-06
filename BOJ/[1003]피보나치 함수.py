t = int(input())

memo = dict()
memo[0] = (1, 0)
memo[1] = (0, 1)

def calc(n):
    if n in memo:
        return memo[n]
    else:
        a = calc(n-1)
        b = calc(n-2)
        memo[n] = (a[0]+b[0], a[1]+b[1])
        return memo[n]

for i in range(t):
    n = int(input())
    res = calc(n)
    print(str(res[0])+' '+str(res[1]))