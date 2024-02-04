N = int(input())
p = [0, 0, 0]

while N % 2 != 0:
    N = N // 2
    p[0] += 1
while N % 3 != 0:
    N = N // 3
    p[0] += 1
while N % 5 != 0:
    N = N // 5
    p[0] += 1

for i in range(sum(p)):
    bunbo *= 5
    bunbo %= 998244353

if N != 1:
    print(0)
else:
    