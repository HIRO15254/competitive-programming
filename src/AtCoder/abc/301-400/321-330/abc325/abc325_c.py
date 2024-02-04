from collections import deque

H, W = map(int, input().split())
ans = 0
inp = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if inp[i][j] == "#":
            ans += 1
            inp[i][j] = "."
            queue = deque()
            queue.append((i, j))
            used = set()
            used.add((i, j))
            while queue:
                x, y = queue.popleft()
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if 0 <= x + dx < H and 0 <= y + dy < W:
                            if (x + dx, y + dy) not in used:
                                if inp[x + dx][y + dy] == "#":
                                    inp[x + dx][y + dy] = "."
                                    queue.append((x + dx, y + dy))
                                    used.add((x + dx, y + dy))
print(ans)
