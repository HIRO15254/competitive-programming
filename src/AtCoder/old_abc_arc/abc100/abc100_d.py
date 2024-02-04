import itertools

N, M = map(int, input().split())
cakes = []
for i in range(N):
    x, y, z = map(int, input().split())
    cakes.append((x, y, z))
ans = 0
for mode in itertools.product((-1, 1), repeat=3):
    val = []
    for cake in cakes:
        val.append(cake[0] * mode[0] + cake[1] * mode[1] + cake[2] * mode[2])
    val.sort(reverse=True)
    ans = max(ans, sum(val[:M]))
print(ans)
