X = input()
val = [0] * len(X)
now = 0
for i in range(len(X)):
    now += int(X[i])
    val[i] = now
for i in range(len(X) - 1):
    j = val[len(X) - i - 1]
    val[len(X) - i - 1] = j % 10
    val[len(X) - i - 2] += j // 10
print("".join(map(str, val)))
