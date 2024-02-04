H, W = map(int, input().split())
A = []
B = []

for _ in range(H):
    A.append(list(input()))
for _ in range(H):
    B.append(list(input()))

last_ans = False
for x_s in range(W):
    for y_s in range(H):
        ans = True
        for x in range(W):
            for y in range(H):
                if A[y][x] != B[(y + y_s) % H][(x + x_s) % W]:
                    ans = False
        last_ans = last_ans or ans
print("Yes" if last_ans else "No")
