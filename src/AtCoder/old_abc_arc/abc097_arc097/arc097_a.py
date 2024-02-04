s = input()
K = int(input())

ans = [""] * K
for i in range(1, min(K + 1, len(s) + 1)): # 文字数
    for j in range(len(s) - i + 1): # 開始位置
        if s[j:j + i] not in ans:
            for k in range(K):
                if s[j:j + i] < ans[k] or ans[k] == "":
                    ans.pop(K - 1)
                    ans.insert(k, s[j:j + i])
                    break
print(ans[K - 1])