import random

IS_TEST = False

N, D, Q = map(int, input().split())
Q_rest = Q
est = list(range(N))
weight = [0] * N
if IS_TEST:
    weight = list(map(int, input().split()))
g = [[] for _ in range(D)]


def query(s, t):
    global Q_rest
    if Q_rest <= 0:
        return "!"
    Q_rest -= 1
    print(len(s), len(t), " ".join(map(str, s)), " ".join(map(str, t)))
    if IS_TEST:
        s_weight = sum([weight[i] for i in s])
        t_weight = sum([weight[i] for i in t])
        if s_weight > t_weight:
            return ">"
        elif s_weight < t_weight:
            return "<"
        else:
            return "="
    return input()


def ans_text():
    ans = [-1] * N
    for i in range(D):
        for j in g[i]:
            ans[j] = i
    return " ".join(map(str, ans))


h = 0
# 3h + 1 間隔
while h <= N / 9:
    h = 3 * h + 1
while h > 0 and Q_rest > max(N, Q // 3):
    for i in range(h, N):
        j = i
        while True:
            if query([est[j]], [est[j - h]]) == "<":
                est[j], est[j - h] = est[j - h], est[j]
                j -= h
                if j < h:
                    break
            else:
                break
        if Q_rest < max(N, Q // 3):
            break
    h = int(h / 3)

for i in range(N):
    if (i // D) % 2 == 0:
        g[i % D].append(est[-(i + 1)])
    else:
        g[(D - 1) - (i % D)].append(est[-(i + 1)])


def omit(li, rep):
    return li[:-rep] + ([] if rep == 1 else li[-rep + 1:])


h = 0
# 3h + 1 間隔
while h <= D / 9:
    h = 3 * h + 1
while h > 0 and Q_rest > max(N, Q // 3):
    for i in range(h, D):
        j = i
        while True:
            if query(g[j], g[j - h]) == "<":
                g[j], g[j - h] = g[j - h], g[j]
                j -= h
                if j < h:
                    break
            else:
                break
        if Q_rest < max(N, Q // 3):
            break
    h = int(h / 3)


step = 0
while Q_rest > 1:
    s = random.randint(0, max(D // 2, D - (Q_rest // N) - 1))
    t = random.randint(min(D // 2, Q_rest // N), D - 1)
    if s == t:
        continue
    ans = query(g[s], g[t])

    if ans == ">":
        if len(g[s]) == 1:
            continue
        rep = 1
        while query(omit(g[s], rep), g[t] + [g[s][-rep]]) == ">" and rep < len(g[s]):
            rep += 1
        if rep > 1:
            rep -= 1
            app = g[s].pop(-rep)
            g[t].append(app)
            g[t].sort(key=lambda x: -est.index(x))
        else:
            rep_2 = 1
            while query(omit(g[s], 1) + [g[t][-rep_2]], omit(g[t], rep_2) + [g[s][-1]]) == "<" and rep_2 < len(g[t]):
                rep_2 += 1
            if rep_2 > 1:
                rep_2 -= 1
                if query(omit(g[s], 1), omit(g[t], rep_2)) == ">":
                    app = g[s].pop(-1)
                    app_2 = g[t].pop(-rep_2)
                    g[t].append(app)
                    g[s].append(app_2)
                    g[t], g[s] = g[s], g[t]
                    g[t].sort(key=lambda x: -est.index(x))
                    g[s].sort(key=lambda x: -est.index(x))
    elif ans == "<":
        if len(g[t]) == 1:
            continue
        rep = 1
        while query(g[s] + [g[t][-rep]], omit(g[t], rep)) == "<" and rep < len(g[t]):
            rep += 1
        if rep > 1:
            rep -= 1
            app = g[t].pop(-rep)
            g[s].append(app)
            g[s].sort(key=lambda x: -est.index(x))
        else:
            rep_2 = 1
            while query(omit(g[s], rep_2) + [g[t][-1]], omit(g[t], 1) + [g[s][-rep_2]]) == ">" and rep_2 < len(g[s]):
                rep_2 += 1
            if rep_2 > 1:
                rep_2 -= 1
                if query(omit(g[s], rep_2), omit(g[t], 1)) == "<":
                    app = g[t].pop(-1)
                    app_2 = g[s].pop(-rep_2)
                    g[s].append(app)
                    g[t].append(app_2)
                    g[t], g[s] = g[s], g[t]
                    g[s].sort(key=lambda x: -est.index(x))
                    g[t].sort(key=lambda x: -est.index(x))
    print("#c", ans_text())
if Q_rest == 1:
    print(1, 1, 0, 1)
print(ans_text())
