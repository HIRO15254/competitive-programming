N, Y = map(int, input().split(" "))
for i in range(Y // 5000 + 1):
    sen = (Y - i * 5000) // 1000
    man_max = i // 2
    gosen_min = i % 2
    if sen + man_max + gosen_min <= N and N <= sen + i:
        print(sen + i - N, 2 * N - 2 * sen - i, sen)
        exit()
print(-1, -1, -1)
