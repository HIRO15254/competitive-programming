N, M, Q = map(int, input().split(" "))
pac = []
box = []
for i in range(N):
    W, V = map(int, input().split(" "))
    pac.append([V, W])
    pac.sort(reverse=True)
box = list(map(int, input().split(" ")))
for i in range(Q):
    ans = 0
    L, R = map(int, input().split(" "))
    box2 = box[:L - 1] + box[R:]
    box_ok = [True] * len(box2)
    box2.sort()
    for k in pac:
        j = 0
        while j < len(box2) and (k[1] > box2[j] or not box_ok[j]):
            j += 1
        if j != len(box2):
            ans += k[0]
            box_ok[j] = False
    print(ans)
