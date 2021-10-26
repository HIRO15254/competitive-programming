N = int(input())
a = list(map(int, input().rstrip().split(" ")))
counter = [0, 0, 0]
for i in a:
    if i % 4 == 0:
        counter[2] += 1
    elif i % 2 == 0:
        counter[1] += 1
    else:
        counter[0] += 1
counter[0] += min(1, counter[1])

if counter[2] + 1 >= counter[0]:
    print("Yes")
else:
    print("No")
