AB_sharp = 0
H_A, W_A = map(int, input().split())
A = []
for i in range(H_A):
    A.append(list(input()))
    AB_sharp += A[i].count('#')
H_B, W_B = map(int, input().split())
B = []
for i in range(H_B):
    B.append(list(input()))
    AB_sharp += B[i].count('#')
H_X, W_X = map(int, input().split())
X = []
for i in range(H_X):
    X.append(list(input()))


def has_a(x, y):
    return 0 <= x < H_A and 0 <= y < W_A


def has_b(x, y):
    return 0 <= x < H_B and 0 <= y < W_B


for A_y in range(-H_A, H_X + 1):
    for A_x in range(-W_A, W_X + 1):
        for B_y in range(-H_B, H_X + 1):
            for B_x in range(-W_B, W_X + 1):
                left = AB_sharp
                ans = True
                for y in range(H_X):
                    for x in range(W_X):
                        if X[y][x] == "#":
                            tmp = False
                            if has_a(y - A_y, x - A_x) and A[y - A_y][x - A_x] == '#':
                                left -= 1
                                tmp = True
                            if has_b(y - B_y, x - B_x) and B[y - B_y][x - B_x] == '#':
                                left -= 1
                                tmp = True
                            if not tmp:
                                ans = False
                        else:
                            if has_a(y - A_y, x - A_x) and A[y - A_y][x - A_x] == '#':
                                ans = False
                            if has_b(y - B_y, x - B_x) and B[y - B_y][x - B_x] == '#':
                                ans = False
                if ans and left == 0:
                    print("Yes")
                    exit()
print("No")
