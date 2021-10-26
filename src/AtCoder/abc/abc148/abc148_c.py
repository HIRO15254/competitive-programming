A, B = map(int, input().split(" "))


def gcd(a, b):
    if(a < b):
        q = a
        a = b
        b = q
    while(b > 0):
        q = a % b
        a = b
        b = q
    return a


def lcm(a, b):
    return a / gcd(a, b) * b


print(int(lcm(A, B)))
