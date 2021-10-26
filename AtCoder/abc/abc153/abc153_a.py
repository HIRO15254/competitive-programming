inp = input().rstrip().split(" ")
HP = int(inp[0])
ATK = int(inp[1])
if HP % ATK == 0:
    print(int(HP / ATK))
else:
    print(int(HP / ATK) + 1)
