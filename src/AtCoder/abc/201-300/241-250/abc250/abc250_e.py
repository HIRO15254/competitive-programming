N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_counter = 0
b_counter = 0
a_set = set()
a_set.add(a[0])
b_set = set()
b_set.add(b[0])
ans = [set() for _ in range(N)]
while a_counter < N and b_counter < N:
    if len(b_set) == len(a_set) and a_set == b_set:
        ans[a_counter].add(b_counter)
        while b_counter + 1 < N and b[b_counter + 1] in b_set:
            b_counter += 1
            ans[a_counter].add(b_counter)
        while a_counter + 1 < N and a[a_counter + 1] in a_set:
            a_counter += 1
            ans[a_counter] = ans[a_counter - 1]
    if len(b_set) < len(a_set) and b_set <= a_set:
        b_counter += 1
        while b_counter < N and b[b_counter] in b_set:
            b_counter += 1
        if b_counter < N:
            b_set.add(b[b_counter])
    else:
        a_counter += 1
        while a_counter < N and a[a_counter] in a_set:
            a_counter += 1
        if a_counter < N:
            a_set.add(a[a_counter])
Q = int(input())
for i in range(Q):
    x, y = map(int, input().split())
    if y - 1 in ans[x - 1]:
        print("Yes")
    else:
        print("No")
