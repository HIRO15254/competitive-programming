N = int(input())
C = input()
counter = [0] * 8
counter[0] = 1
target = "atcoder"
for i in range(N):
    for j in range(len(target)):
        if C[i] == target[j]:
            counter[j + 1] += counter[j]
            counter[j + 1] %= 10 ** 9 + 7
print(counter[-1])
