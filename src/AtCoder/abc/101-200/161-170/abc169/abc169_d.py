N = int(input())
now = 2
counter = 0
k = []
ans = 0
while N != 1:
    if N % now == 0:
        N = N // now
        counter += 1
    else:
        now += 1
        if N < now ** 2:
            k.append(counter)
            counter = 1
            break
        if counter != 0:
            k.append(counter)
            counter = 0
k.append(counter)
for i in range(len(k)):
    counter = 2
    while k[i] > 0:
        k[i] -= counter
        counter += 1
    ans += counter - 2
print(ans)
