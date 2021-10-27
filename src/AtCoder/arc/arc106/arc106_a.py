N = int(input())
th = [1]
fi = [1]
while th[-1] <= 10 ** 18:
    th.append(th[-1] * 3)
while fi[-1] <= 10 ** 18:
    fi.append(fi[-1] * 5)

fl = False
for i in range(1, len(th)):
    for j in range(1, len(fi)):
        if th[i] + fi[j] == N:
            print(i, j)
            fl = True
            break
    if fl:
        break
else:
    print(-1)
