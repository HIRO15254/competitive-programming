from collections import deque

H, W = map(int, input().split())

m = []
for i in range(H):
    m.append(list(input()))

c = 0
for y in range(H):
    for x in range(W):
        if m[y][x] == "#":
            m[y][x] = c
            q = deque([(y, x)])
            while q:
                y2, x2 = q.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x2 + dx, y2 + dy
                    if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == "#":
                        m[ny][nx] = c
                        q.append((ny, nx))
            c += 1

ans_bunsi = 0
ans_bunbo = 0

for y in range(H):
    for x in range(W):
        if m[y][x] == ".":
            s = set()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= ny < H and 0 <= nx < W and m[ny][nx] != ".":
                    s.add(m[ny][nx])
            ans_bunsi += c + 1 - len(s)
            ans_bunbo += 1
print((ans_bunsi * pow(ans_bunbo, -1, 998244353)) % 998244353)
