def update_w(x, ans_w, ans_h, graph_w, graph_h):
    ans_w[x] = True
    for i in graph_w[x]:
        if not ans_h[i]:
            update_h(i, ans_w, ans_h, graph_w, graph_h)


def update_h(y, ans_w, ans_h, graph_w, graph_h):
    ans_h[y] = True
    for i in graph_h[y]:
        if not ans_w[i]:
            update_w(i, ans_w, ans_h, graph_w, graph_h)


while True:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
    ans_w = [False] * w
    ans_h = [False] * h
    graph_w = [[] for _ in range(w)]
    graph_h = [[] for _ in range(h)]
    for i in range(w + h - 1):
        x, y, n = list(map(int, input().split()))
        graph_w[x - 1].append(y - 1)
        graph_h[y - 1].append(x - 1)
    update_w(0, ans_w, ans_h, graph_w, graph_h)
    if ans_w.count(False) == 0 and ans_h.count(False) == 0:
        print("YES")
    else:
        print("NO")
