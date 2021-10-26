A = list(map(int, input().rstrip().split(" ")))
for i in range(5):
    if A[i] == 0:
        print(i + 1)
        break
