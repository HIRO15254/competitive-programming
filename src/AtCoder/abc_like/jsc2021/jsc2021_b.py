N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
ans = [0] * (10 ** 3 + 1)
a_2 = ""
for i in A:
    ans[i] += 1
for i in B:
    ans[i] += 1
for i in range(10 ** 3 + 1):
    if ans[i] == 1:
        if a_2 != "":
            a_2 += " "
        a_2 += str(i)
print(a_2)
