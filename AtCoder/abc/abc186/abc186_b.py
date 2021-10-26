H, W = map(int, input().split(" "))
A = []
for i in range(H):
    A += list(map(int, input().split(" ")))
print(sum(A) - H * W * min(A))
