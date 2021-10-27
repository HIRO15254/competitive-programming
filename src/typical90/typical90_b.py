bra = [set() for _ in range(10)]
bra[0].add("()")
for i in range(1, 10):
    for j in bra[i - 1]:
        bra[i].add("(" + j + ")")
    for j in range(i):
        for k in bra[j]:
            for m in bra[i - j - 1]:
                bra[i].add(k + m)
N = int(input())
if N % 2 == 0:
    ans_lis = sorted(list(bra[(N - 2) // 2]))
    for i in ans_lis:
        print(i)
else:
    print()
