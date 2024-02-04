S = list(input())
k = 0
for i in S:
    k += int(i)
if k % 9 == 0:
    print("Yes")
else:
    print("No")
