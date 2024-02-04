N, K = map(int, input().split())
S = input()


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


d = make_divisors(N)
ans = N
alp = "abcdefghijklmnopqrstuvwxyz"
for i in d:
    l = []
    length = N // i
    for j in range(i):
        l.append(S[length * j:length * (j + 1)])
    need = 0
    for j in range(length):
        c = [0] * 26
        for k in range(i):
            c[alp.index(l[k][j])] += 1
        need += i - max(c)
    if need <= K:
        ans = min(ans, length)
print(ans)
