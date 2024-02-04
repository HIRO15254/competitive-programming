N = int(input())
A_full_set = set()
A_dict = dict()
A_set = set()


def text_times(x, y):
    ans = []
    kuri = 0
    for i in range(len(x)):
        d = int(x[-(i + 1)]) * int(y) + kuri
        ans.append(str(d % 10))
        kuri = d // 10
    if kuri:
        ans.append(str(kuri))
    return "".join(ans[::-1])


def text_plus(x, y):
    ans = []
    kuri = 0
    if len(x) < len(y):
        x, y = y, x
    y = y.zfill(len(x))
    for i in range(len(x)):
        d = int(x[-(i + 1)]) + int(y[-(i + 1)]) + kuri
        ans.append(str(d % 10))
        kuri = d // 10
    if kuri:
        ans.append(str(kuri))
    return "".join(ans[::-1])


def text_prod(x, y):
    now = "0"
    for i in range(len(y)):
        now = text_plus(now, text_times(x, y[-(i + 1)]) + "0" * i)
    return now


for i in range(N):
    a = input()
    if a in A_full_set:
        A_dict[a] += 1
    else:
        A_dict[a] = 1
        A_full_set.add(a)
    for i in range(max(len(a) // 10, 10)):
        A_set.add(a[-((i + 1) * 10):])

ans = 0
for x in A_full_set:
    for y in A_full_set:
        if len(x) + len(y) > 1001:
            continue
        for i in range(1, max((len(x) + len(y) - 1) // 10, 10)):
            c = text_prod(x[min(-i * 10, -len(x)):], y[min(-i * 10, -len(y)):])[(-i * 10):]
            if c not in A_set:
                break
        else:
            now = text_prod(x, y)
            if now in A_full_set:
                ans += A_dict[x] * A_dict[y] * A_dict[now]
print(ans)
