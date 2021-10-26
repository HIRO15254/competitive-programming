A = []
for i in range(28):
    A.append(int(input()))
for i in range(1, 31):
    if i not in A:
        print(i)
