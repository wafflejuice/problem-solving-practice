import sys

sys.setrecursionlimit(10**6)
a, b = map(int, sys.stdin.readline().rstrip().split())

def gcd_recursive(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(a-b, b)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))