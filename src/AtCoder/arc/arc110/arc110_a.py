def gcd(a, b):
    if(a < b):
        q = a
        a = b
        b = q
    while(b > 0):
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a / gcd(a, b) * b


N = int(input())

ans = 1
for i in range(1, N + 1):
    ans = lcm(ans, i)
ans += 1
print(int(ans))
