H, W = map(int, input().split())
a = [-1, -1]
b = [-1, -1]
for y in range(H):
    inp = list(input())
    for x in range(W):
        if inp[x] == "o":
            if a[0] == -1:
                a = [x, y]
            else:
                b = [x, y]
print(abs(a[0] - b[0]) + abs(a[1] - b[1]))
