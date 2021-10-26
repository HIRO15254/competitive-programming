H, W = map(int, input().split(" "))
for _ in range(H):
    q = [-1] * W
    c = -1
    A = list(input())
    for i in range(W):
        if A[i] == "c":
            c = 0
        else:
            if c != -1:
                c += 1
        q[i] = c
    print(" ".join(map(str, q)))
