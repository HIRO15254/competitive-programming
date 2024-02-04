N = int(input())
dic = dict()
for _ in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 0
    if dic[s] == 0:
        print(s)
    else:
        print(f'{s}({dic[s]})')
