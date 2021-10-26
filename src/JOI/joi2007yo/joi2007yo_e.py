A, B, C = map(int, input().rstrip().split(" "))
N = int(input())
case_true = []
case_false = []
val_list = [2 for i in range(A + B + C)]

for i in range(N):
    a, b, c, r = map(int, input().rstrip().split(" "))
    if r == 1:
        case_true.append([a, b, c])
    else:
        case_false.append([a, b, c])

for a, b, c in case_true:
    val_list[a - 1] = 1
    val_list[b - 1] = 1
    val_list[c - 1] = 1

for a, b, c in case_false:
    if val_list[a - 1] == 2 and val_list[b - 1] == 1 and val_list[c - 1] == 1:
        val_list[a - 1] = 0
    if val_list[a - 1] == 1 and val_list[b - 1] == 2 and val_list[c - 1] == 1:
        val_list[b - 1] = 0
    if val_list[a - 1] == 1 and val_list[b - 1] == 1 and val_list[c - 1] == 2:
        val_list[c - 1] = 0

for i in range(A + B + C):
    print(val_list[i])
