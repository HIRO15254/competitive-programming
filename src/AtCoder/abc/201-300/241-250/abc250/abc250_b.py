N, A, B = map(int, input().split())
ans_a = ""
ans_b = ""
for i in range(N):
    if i % 2 == 0:
        ans_a += "." * B
        ans_b += "#" * B
    else:
        ans_a += "#" * B
        ans_b += "." * B
for i in range(N):
    for j in range(A):
        if i % 2 == 0:
            print(ans_a)
        else:
            print(ans_b)
