N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
A_count = []
A.sort()
now = A[0]
counter = 1
for i in A[1:]:
    if now == i:
        counter += 1
    else:
        A_count.append(counter)
        now = i
        counter = 1
A_count.append(counter)
A_count.sort()
print(sum(A_count[0:len(A_count) - K]))
