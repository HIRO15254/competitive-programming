import itertools
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

ans = 10 ** 18
for i in itertools.permutations(range(D)):
    score = 0
    count = 0
    for j in i:
        p = problems[j]
        if score + p[0] * (j + 1) * 100 >= G:
            count += (G - score - 1) // ((j + 1) * 100) + 1
            break
        else:
            score += p[0] * (j + 1) * 100 + p[1]
            count += p[0]
            if score >= G:
                break
    ans = min(ans, count)
print(ans)
