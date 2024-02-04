S = input()
now = S[0]
count = 0
lis = []
for i in S:
    if i == now:
        count += 1
    else:
        if now == "0":
            now = "1"
        else:
            now = "0"
        lis.append(count)
        count = 1
lis.append(count)
print(lis)
lis_2 = [10 ** 18]
for i in range(len(lis) - 1):
    lis_2.append(lis[i] + lis[i + 1])
print(min(max(lis), min(lis_2)))
