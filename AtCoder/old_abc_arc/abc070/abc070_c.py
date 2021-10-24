def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
ans = int(input())
for i in range(N - 1):
    ans = lcm(ans, int(input()))
print(ans)
